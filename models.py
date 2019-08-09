from flask_sqlalchemy import SQLAlchemy
from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash

db = SQLAlchemy()

# code citation: Flask Mega Tutorial and Flask Manual pages

class User(UserMixin, db.Model):
    __tablename__ = 'user'
    user_id = db.Column(db.Integer, primary_key=True, autoincrement=True)
    first_name = db.Column(db.String(64))
    last_name = db.Column(db.String(64))
    username = db.Column(db.String(32), nullable=False)
    hashed_password = db.Column(db.String(128), nullable=False)

    def get_id(self):
        return (self.user_id)


class Photos(db.Model):
    __tablename__ = 'photos'
    mlsnum = db.Column(db.Integer, db.ForeignKey('properties.mlsnum'), primary_key=True, nullable=False)
    imgnum = db.Column(db.Integer, primary_key=True, nullable=False)
    features = db.Column(db.String(4000))


class Properties(db.Model):
    __tablename__ = 'properties'
    mlsnum = db.Column(db.Integer, primary_key=True, autoincrement=True)
    status = db.Column(db.String(3))
    soldprice = db.Column(db.Integer)
    listprice = db.Column(db.Integer)
    listdate = db.Column(db.DateTime)
    solddate = db.Column(db.DateTime)
    expireddate = db.Column(db.DateTime)
    dom = db.Column(db.Integer)
    dto = db.Column(db.Integer)
    address = db.Column(db.String(254)) 
    city = db.Column(db.String(254))
    state = db.Column(db.String(2))
    zipcode = db.Column(db.Integer) ## this was zip in db, may need to change
    area = db.Column(db.String(254))
    beds = db.Column(db.Integer)
    baths = db.Column(db.Integer)
    sqft = db.Column(db.Integer)
    age = db.Column(db.Integer)
    lotsize = db.Column(db.Integer)
    agentname = db.Column(db.String(254)) 
    officename = db.Column(db.String(254)) 
    officephone = db.Column(db.String(254))
    showinginstructions = db.Column(db.String(1024))
    remarks = db.Column(db.String(4000))
    style = db.Column(db.String(254)) 
    level = db.Column(db.Integer)
    garage = db.Column(db.Integer)
    heating = db.Column(db.String(254)) 
    cooling = db.Column(db.String(254)) 
    elementaryschool = db.Column(db.String(254)) 
    juniorhighschool = db.Column(db.String(254)) 
    highschool = db.Column(db.String(254)) 
    otherfeatures = db.Column(db.String(4000)) 
    proptype = db.Column(db.String(2)) 
    streetname = db.Column(db.String(254)) 
    housenum1 = db.Column(db.Integer)
    housenum2 = db.Column(db.String(254)) 
    photourl = db.Column(db.String(254)) 

