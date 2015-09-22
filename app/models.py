from . import db

class Coordinate(db.Model):
    __tablename__ = 'coordinates'
    id = db.Column(db.Integer, primary_key = True)
    latitude = db.Column(db.Float)
    longitude = db.Column(db.Float)
    notes = db.Column(db.String(64))

    def __repr__(self):
        return '{ latitude: ', self.latitude ,', longitude: ', self.longitude, ', notes: ',self.notes,'}'
