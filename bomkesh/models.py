import enum
from bomkesh import db
from sqlalchemy.sql import func


class PacketTypeEnum(enum.Enum):
    TCP = "TCP"
    UDP = "UDP"


class RawPacket(db.Model):
    __tablename__ = "rawpacket"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    source_ip = db.Column(db.String(), nullable=False)
    destination_ip = db.Column(db.String(), nullable=False)
    source_port = db.Column(db.Integer(), nullable=False)
    destination_port = db.Column(db.Integer(), nullable=False)
    packet_type = db.Column(
        db.Enum(PacketTypeEnum), default=PacketTypeEnum.TCP, nullable=False
    )
    timestamp = db.Column(
        db.DateTime(timezone=True), default=func.now(), nullable=False
    )

    def __init__(
        self,
        source_ip,
        destination_ip,
        source_port,
        destination_port,
        packet_type,
        timestamp,
    ):
        self.source_ip = source_ip
        self.destination_ip = destination_ip
        self.source_port = source_port
        self.destination_port = destination_port
        self.packet_type = packet_type
        self.timestamp = timestamp

    def __repr__(self):
        return "{} <packets: {} => {}>".format(
            self.packet_type, self.source_ip, self.destination_ip
        )


class Dnsqueue(db.Model):
    __tablename__ = "dnsqueue"

    id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    domain_name = db.Column(db.String(), nullable=False)
    domain_class = db.Column(db.String(), nullable=False)
    domain_type = db.Column(db.String(), nullable=False)
    ip_a = db.Column(db.String(), nullable=False)
    timestamp = db.Column(
        db.DateTime(timezone=True), default=func.now(), nullable=False
    )

    def __init__(self, domain_name, domain_class, domain_type, ip, timestamp):
        self.domain_name = domain_name
        self.domain_class = domain_class
        self.domain_type = domain_type
        self.ip_a = ip
        self.timestamp = timestamp

    def __repr__(self):
        return "<domain: {}>".format(self.domain_name)
