
import urllib.request
import os.path


def gen_redis_proto(*cmd):
    proto = '*{0}\r\n'.format(len(cmd))
    for c in cmd:
        proto += '${0}\r\n'.format(len(c))
        proto += '{0}\r\n'.format(c)

    return proto


DYNAMIC_DNS_URL = 'https://gist.githubusercontent.com/neu5ron/8dd695d4cb26b6dcd997/raw/d838cc55e9de34b283cd9b1f3822b53a2d8c5c0a/dynamic-dns.txt'

def dynamicdns_to_redis(fh):

    res = urllib.request.urlopen(DYNAMIC_DNS_URL)

    for line in res:
        domains = line.split(b'#')
    
        for domain in domains:
            fh.write(gen_redis_proto('sadd', 'dynamicdns', str(domain.strip(), 'utf-8')))


MAJESTIC_MILLION_URL = 'http://downloads.majestic.com/majestic_million.csv'


def majestic_to_redis(fh):

    res = urllib.request.urlopen(MAJESTIC_MILLION_URL)

    firstLine = True

    for line in res:
        if firstLine:
            firstLine = False
            continue

        domain = line.split(b',')[2]

        fh.write(gen_redis_proto('sadd', 'majestic', str(domain, 'utf-8')))



if __name__ == '__main__':

    with open('appendonly.aof', 'w') as fh:
        fh.write('*2\r\n$6\r\nSELECT\r\n$1\r\n0\r\n') # select 0 in redis-speak
        dynamicdns_to_redis(fh)
        majestic_to_redis(fh)


