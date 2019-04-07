#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-天底 ガジ'


Message = """
from tools.time_format import time_format


class Message(sdb.Model):
    id = sdb.Column(sdb.Integer, primary_key=True)
    body = sdb.Column(sdb.Text, nullable=False)
    sender = sdb.Column(sdb.String(80), unique=False, nullable=False)
    pub_date = sdb.Column(
        sdb.String(25), nullable=False, default=time_format
    )

    def __repr__(self):
        return '<Message %r>' % self.body


class MessageSchema(sma.Schema):
    class Meta:
        model = Message
        fields = ('id', 'body', 'sender', 'pub_date')
"""
