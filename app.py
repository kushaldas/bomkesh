from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy
import redis
import json
import os


app = Flask(__name__)
app.config['SQLALCHEMY_DATABASE_URI'] = os.environ['DATABASE_URL']
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False
db = SQLAlchemy(app)

from models import Dnsqueue, TCPPacket


def init_redis():
    return redis.Redis(
        host='localhost',
        port=6379,
        db=0
    )


@app.route('/dnsqueue')
def dnsqueue():
    return render_template('dns_list.html')

@app.route('/fetch-dns')
def fetch_dns():
    redis_db = init_redis()
    pipe = redis_db.pipeline()
    pipe.lrange('dnsqueue', 0, 9)
    pipe.ltrim('dnsqueue', 10, -1)
    dns_data, trim_success = pipe.execute()
    dns_data_json = [json.loads(data) for data in dns_data]
    return jsonify(dns_data=dns_data_json)
    


if __name__ == "__main__":
    app.run(debug=True, host="0.0.0.0")
