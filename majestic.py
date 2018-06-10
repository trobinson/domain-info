
import urllib.request
import os.path

MAJESTIC_MILLION_URL = 'http://downloads.majestic.com/majestic_million.csv'


def load_majestic(redis, filename=None):

    if filename and os.path.exists(filename):
        with open(filename) as fh:
            res = [bytes(l, 'utf-8') for l in fh.readlines()]
    else:
        res = urllib.request.urlopen(MAJESTIC_MILLION_URL)

    firstLine = True

    for line in res:
        if firstLine:
            firstLine = False
            continue

        domain = line.split(b',')[2]

        redis.sadd('majestic', domain)

