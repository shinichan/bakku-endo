#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-天底 ガジ'

from flask import Flask, request
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

from models.client import Message
from config.base_config import BaseConfig, AppConfig


# first_or_404(). This will raise 404 errors instead of returning None
from werkzeug.exceptions import NotFound


app = Flask(__name__)
app.config.from_object(BaseConfig)

api = Api(app)
sdb = SQLAlchemy(app)


# MODELS
exec(Message)


class SimpleGet(Resource):

    def get(self, query_like):
        # Message.sender.endswith(query_like)
        m = Message.query.filter_by(
            sender=f's{query_like}'
        ).first()

        # must know if data exists or not
        if m:
            return {
                query_like: {
                    'id': m.id,
                    'body': m.body,
                    'sender': m.sender,
                    'pub_date': AppConfig.TIME_TEMPLATE.format(
                        m.pub_date, AppConfig.DAYS[m.pub_date.weekday()]
                    )
                }
            }
        else:
            raise NotFound

    def put(self, query_like):
        # sender, body = request.form['data']
        # m = Message(sender, body)
        # sdb.session.add(m)
        # sdb.session.commit()
        # return {query_like: {sender: body}}
        pass


api.add_resource(SimpleGet, '/<string:query_like>')


if __name__ == '__main__':
    app.run(debug=True)
