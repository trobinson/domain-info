
import urllib.request
import os.path

DYNAMIC_DNS_URL = 'https://gist.githubusercontent.com/neu5ron/8dd695d4cb26b6dcd997/raw/d838cc55e9de34b283cd9b1f3822b53a2d8c5c0a/dynamic-dns.txt'

def load_dynamicdns(redis, filename=None):

    if filename and os.path.exists(filename):
        with open(filename) as fh:
            res = [bytes(l, 'utf-8') for l in fh.readlines()]
    else:
        res = urllib.request.urlopen(DYNAMIC_DNS_URL)

    for line in res:
        domains = line.split(b'#')
        
        for domain in domains:
            redis.sadd('dynamicdns', domain.strip())
