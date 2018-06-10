
from flask import Flask, jsonify
import redis

from majestic import load_majestic
from dynamicdns import load_dynamicdns

# init flask and redis
app = Flask(__name__)
r = redis.StrictRedis(host='redis', port=6379, db=0)

# init data in redis
load_majestic(r, filename='data/majestic_million.csv')
load_dynamicdns(r, filename='data/dynamic-dns.txt')


@app.route('/majestic/<domain>')
def majestic(domain):
    return jsonify({domain: r.sismember('majestic', domain)})

@app.route('/dynamicdns/<domain>')
def dynamicdns(domain):
    return jsonify({domain: r.sismember('dynamicdns', domain)})


