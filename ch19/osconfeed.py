from urllib.request import urlopen
import warnings
import os
import json


"""
>>> feed = load()
>>> sorted(feed['Schedule'].keys())
['conferences', 'events', 'speakers', 'venues']
>>> for key, value in sorted(feed['Schedule'].items()):
...     print('{:3} {}'.format(len(value), key))
... 
  1 conferences
494 events
357 speakers
 53 venues
>>> feed['Schedule']['speakers'][-1]['name']
'Carina C. Zona'
>>> feed['Schedule']['speakers'][-1]['serial']
141590
>>> feed['Schedule']['events'][40]['name']
'There *Will* Be Bugs'
>>> feed['Schedule']['events'][40]['speakers']
[3471, 5199]

"""


URL = 'http://www.oreilly.com/pub/sc/osconfeed'
JSON = 'data/osconfeed.json'


def load():
    if not os.path.exists(JSON):
        msg = 'downloading {} to {}'.format(URL, JSON)
        warnings.warn(msg)
        with urlopen(URL) as remote, open(JSON, 'wb') as local:
            local.write(remote.read())

    with open(JSON) as fp:
        return json.load(fp)
