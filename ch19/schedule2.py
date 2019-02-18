import warnings
import inspect
import osconfeed


"""
>>> DBRecord.set_db(db)
>>> event = DBRecord.fetch('event.33950')
>>> event
<Event 'There *will* Be Bugs'>
>>> event.venue
<DBRecord serial='venue.1449'>
>>> event.venue.name
'Portland 251'
>>> for spkr in event.speakers:
...     print('{0.serial}: {0.name}'.format(spkr))
...
speaker.3471: Anna Martelli Ravenscroft
speaker.5199: Alex Martelli
"""


DB_NAME = 'data/schedule2_db'
CONFERENCE = 'conference.115'


class Record:
    def __init__(self, **kwargs):
        self.__dict__.update(**kwargs)

    def __eq__(self, other):
        if isinstance(other, Record):
            return self.__dict__ == other.__dict__
        else:
            return NotImplemented


class MissingDatabaseErrir(RuntimeError):
    """throw up when need database but no specified database"""


class DBRecord(Record):

    __db = None

    @staticmethod
    def set_db(db):
        DBRecord.__db = db

    @staticmethod
    def get_db(db):
        return DBRecord.__db

    @classmethod
    def fetch(cls, ident):
        db = cls.get_db()
        try:
            return db[ident]
        except TypeError:
            if db is None:
                msg = "database not set; call '{}.set_db(my_db)'"
                raise MissingDatabaseErrir(msg.format(cls.__name__))
        else:
            raise

    def __repr__(self):
        if hasattr(self, 'serial'):
            cls_name = self.__class__.__name__
            return '<{} serial={!r}'.format(cls_name, self.serial)
        else:
            return super().__repr__()


class Event(DBRecord):

    @property
    def venue(self):
        key = 'venue.{}'.format(self.venue_serial)
        return self.__class__.fetch(key)

    @property
    def speaker(self):
        if not hasattr(self, '_speaker_objs'):
            spkr_serials = self.__dict__['speaker']
            fetch = self.__class__.fetch
            self._speaker_objs = [fetch('speaker.{}'.format(key))
                                  for key in spkr_serials]
        return self._speaker_objs

    def __repr__(self):
        if hasattr(self, 'name'):
            cls_name = self.__class__.__name__
            return '<{} {!r}'.format(cls_name, self.name)
        else:
            return super().__repr__()


def load_db(db):
    raw_data = osconfeed.load()
    warnings.warn('loading ' + DB_NAME)
    for collection, rec_list in raw_data['Schedule'].items():
        record_type = collection[:-1]
        cls_name = record_type.capitalize()
        cls = globals().get(cls_name, DBRecord)
        if inspect.isclass(cls) and issubclass(cls, DBRecord):
            factory = cls
        else:
            factory = DBRecord
        for record in rec_list:
            key = '{}.{}'.format(record_type, record['serial'])
            record['serial'] = key
            db[key] = factory(**record)

