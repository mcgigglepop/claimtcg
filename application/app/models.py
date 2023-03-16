from flask_login import UserMixin
from werkzeug.security import generate_password_hash, check_password_hash
from app import db, login

# user model
class User(UserMixin, db.Model):
    id = db.Column(db.Integer, primary_key=True)
    firstName = db.Column(db.String(128))
    lastName = db.Column(db.String(128))
    email = db.Column(db.String(120), index=True, unique=True)
    passwordHash = db.Column(db.String(128))
    currentMfaCode = db.Column(db.Integer)
    userIdHash = db.Column(db.String(64))
    isVerified = db.Column(db.Boolean, default=False)
    collectionCount = db.Column(db.Integer, default=0)
    collections = db.relationship('Collection', backref='author', lazy='dynamic')
    
    def __repr__(self):
        return '<User {}>'.format(self.email)

    def setPassword(self, password):
        self.passwordHash = generate_password_hash(password)

    def checkPassword(self, password):
        return check_password_hash(self.passwordHash, password)

    def getEmail(self):
        return self.email

    def getCurrentMfaCode(self):
        return self.currentMfaCode

    def getUserIdHash(self):
        return self.userIdHash

    def getName(self):
        return f'{self.firstName} {self.lastName}'
    
    def getCollectionCount(self):
        return self.collectionCount
    
    def getCollections(self):
        return Collection.query.filter_by(user_id=self.id).all()