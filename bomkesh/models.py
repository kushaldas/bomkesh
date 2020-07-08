from bomkesh import db
from sqlalchemy.sql import func


class TCPPacket(db.Model):
    __tablename__ = 'tcppacket'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    source_ip = db.Column(db.String())
    destination_ip = db.Column(db.String())
    source_port = db.Column(db.Integer())
    destination_port = db.Column(db.Integer())
    timestamp = db.Column(db.DateTime(timezone=True), default=func.now())

    def __init__(self, source_ip, destination_ip, source_port, destination_port, timestamp):
        self.source_ip = source_ip
        self.destination_ip = destination_ip
        self.source_port = source_port
        self.destination_port = destination_port
        self.timestamp = timestamp

    def __repr__(self):
        return '<packets: {} => {}>'.format(self.source_ip, self.destination_ip)


class Dnsqueue(db.Model):
    __tablename__ = 'dnsqueue'

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    domain_name = db.Column(db.String())
    domain_class = db.Column(db.String())
    domain_type = db.Column(db.String())
    ip_a = db.Column(db.String())
    timestamp = db.Column(db.DateTime(timezone=True), default=func.now())

    def __init__(self, domain_name, domain_class, domain_type, ip, timestamp):
        self.domain_name = domain_name
        self.domain_class = domain_class
        self.domain_type = domain_type
        self.ip_a = ip
        self.timestamp = timestamp

    def __repr__(self):
        return '<domain: {}>'.format(self.domain_name)