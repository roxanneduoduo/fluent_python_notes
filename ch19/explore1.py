from collections import abc
import keyword


"""
>>> from osconfeed import load
>>> raw_feed = load()
>>> feed = FrozenJSON(raw_feed)
>>> len(feed.Schedule.speakers)
357
>>> sorted(feed.Schedule.keys())
['conferences', 'events', 'speakers', 'venues']
>>> for key, value in sorted(feed.Schedule.items()):
...     print('{:3} {}'.format(len(value), key))
... 
  1 conferences
494 events
357 speakers
 53 venues
>>> feed.Schedule.speakers[-1].name
'Carina C. Zona'
>>> talk = feed.Schedule.events[40]
>>> type(talk)
<class 'explore0.FrozenJSON'>
>>> talk.name
'There *Will* Be Bugs'
>>> talk.speakers
[3471, 5199]
>>> talk.flavor
Traceback (most recent call last):
  ...
KeyError: 'flavor'

"""


class FrozenJSON:
    """A read-only interface, use attribute represent method to access JSON class object
    """

    def __init__(self, mapping):
        self.__data = {}
        for key, value in mapping.items():
            if keyword.iskeyword(key):
                key += '_'
            self.__data[key] = value

    def __getattr__(self, name):
        if hasattr(self.__data, name):
            return getattr(self.__data, name)
        else:
            return FrozenJSON.build(self.__data[name])

    @classmethod
    def build(cls, obj):
        if isinstance(obj, abc.Mapping):
            return cls(obj)
        elif isinstance(obj, abc.MutableSequence):
            return [cls.build(item) for item in obj]
        else:
            return obj

