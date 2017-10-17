#!/usr/bin/python3
from app import db

class User(db.Model):
    id = db.Column(db.Integer,primary_key=True)
    nickname = db.Column(db.VARCHAR(64),index=True,unique=True)
    email = db.Column(db.VARCHAR(120),index=True,unique=True)

    def __repr__(self):
        return '<User %r>' % (self.nickname)

