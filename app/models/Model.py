import datetime

from app import db


class Record(db.Model):
    __tablename__ = 'record'

    id = db.Column(db.Integer, primary_key=True, nullable=True)
    origin = db.Column(db.String(255), unique=False, nullable=True)
    updated = db.Column(db.DateTime, default=datetime.datetime.now(), onupdate=datetime.datetime.now())
    name = db.Column(db.String(255), unique=False, nullable=True)
    url = db.Column(db.String(255), nullable=True)
    api_url = db.Column(db.String(255), nullable=True)
    tagline = db.Column(db.String(1000), nullable=True)
    mission = db.Column(db.String(1000), nullable=True)
    node_types = db.Column(db.String(1000), nullable=True)
    location = db.Column(db.String(255), nullable=True)
    lat = db.Column(db.Float, nullable=True)
    long = db.Column(db.Float, nullable=True)
    networks = db.Column(db.String(1000), nullable=True)
    tags = db.Column(db.String(1000), nullable=True)
    feed = db.Column(db.String(500), nullable=True)

    def __init__(self, origin="Index", updated=None, name=None, url=None, api_url=None, tagline=None, mission=None,
                 node_types=None, location=None,
                 lat=None, long=None, networks=None, feed=None):
        self.origin = origin
        self.updated = updated
        self.api_url = api_url
        self.tagline = tagline
        self.mission = mission
        self.location = location
        self.name = name
        self.origin = origin
        self.url = url
        self.node_types = node_types
        self.lat = lat
        self.long = long
        self.networks = networks
        self.feed=feed

    def save_record(self):
        """ Updates Record object """
        db.session.add(self)
        db.session.commit()
