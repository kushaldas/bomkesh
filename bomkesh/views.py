import json
from flask import render_template, jsonify
from config import init_redis

from bomkesh import app
from bomkesh.models import Dnsqueue, RawPacket


@app.route("/dnsqueue")
def dnsqueue():
    return render_template("dns_list.html")


@app.route("/tcpqueue")
def tcpqueue():
    return render_template("tcp_list.html")


@app.route("/fetch-dns")
def fetch_dns():
    redis_db = init_redis()
    pipe = redis_db.pipeline()
    pipe.lrange("dnsqueue", 0, 9)
    pipe.ltrim("dnsqueue", 10, -1)
    dns_data, trim_success = pipe.execute()
    dns_data_json = [json.loads(data) for data in dns_data]
    return jsonify(dns_data=dns_data_json)
