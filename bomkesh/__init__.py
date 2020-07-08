from flask import Flask, render_template, jsonify
from flask_sqlalchemy import SQLAlchemy

from config import DevelopmentConfig

app = Flask(__name__)
app.config.from_object(DevelopmentConfig)

db = SQLAlchemy(app)

from bomkesh.views import dnsqueue, tcpqueue, fetch_dns
