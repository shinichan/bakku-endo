#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-天底 ガジ'

from os import getcwd
from sys import platform
from os.path import join
from datetime import datetime

from flask import Flask
from flask_sqlalchemy import SQLAlchemy


app = Flask(__name__)


# http://flask-sqlalchemy.pocoo.org/2.3/config/
slash = '/' * (3 if 'win' in platform else 4)

app.config['SQLALCHEMY_DATABASE_URI'] = "sqlite:{}{}".format(
    slash, join(getcwd(), 'st.db')
)
app.config['SQLALCHEMY_TRACK_MODIFICATIONS'] = False

db = SQLAlchemy(app)
# write funcs for query: http://flask-sqlalchemy.pocoo.org/2.3/customizing/


class Message(db.Model):
    """
    >>> db.create_all()
    >>> from sql_start import Message
    >>> f = Message(
    ...     body='posting test data to the sql database',
    ...     sender='someone'
    ... )
    >>> db.session.add(f)
    >>> db.session.commit()
    >>> Message.query.all()
    [<Message 'posting test data to the sql database'>]
    >>>

    def com(f):
        db.session.add(f)
        db.session.commit()

    for item in range(1, 14):
        f = Message(body=f'bla {item}', sender=f's{item}')
        com(f)
    """

    id = db.Column(db.Integer, primary_key=True)
    body = db.Column(db.Text, nullable=False)
    sender = db.Column(db.String(80), unique=True, nullable=False)
    pub_date = db.Column(db.DateTime, nullable=False, default=datetime.utcnow)

    def __repr__(self):
        return '<Message %r>' % self.body
