
from flask import Flask, jsonify
import redis

# init flask and redis
app = Flask(__name__)
r = redis.StrictRedis(host='redis', port=6379, db=0)

@app.route('/majestic/<domain>')
def majestic(domain):
    return jsonify({domain: r.sismember('majestic', domain)})

@app.route('/dynamicdns/<domain>')
def dynamicdns(domain):
    return jsonify({domain: r.sismember('dynamicdns', domain)})


