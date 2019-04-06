#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-天底 ガジ'


Message = """
from datetime import datetime


class Message(sdb.Model):
    id = sdb.Column(sdb.Integer, primary_key=True)
    body = sdb.Column(sdb.Text, nullable=False)
    sender = sdb.Column(sdb.String(80), unique=True, nullable=False)
    pub_date = sdb.Column(
        sdb.DateTime, nullable=False, default=datetime.utcnow()
    )

    def __repr__(self):
        return '<Message %r>' % self.body
"""
