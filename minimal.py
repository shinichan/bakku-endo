#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-天底 ガジ'

from flask import Flask, request, jsonify
from flask_restful import Resource, Api
from flask_sqlalchemy import SQLAlchemy

from flask_marshmallow import Marshmallow

from models.client import Message
from config.base_config import BaseConfig

# first_or_404(). This will raise 404 errors instead of returning None
from werkzeug.exceptions import NotFound

# from tools import time_format


app = Flask(__name__)
app.config.from_object(BaseConfig)

api = Api(app)
sdb = SQLAlchemy(app)
sma = Marshmallow(app)


# MODELS
exec(Message)


class SimpleRest(Resource):

    def get(self, query_like):
        # Message.sender.endswith(query_like)
        m = Message.query.filter_by(
            id=query_like
        ).first()

        # must know if data exists or not
        if m:
            return {
                query_like: {
                    'id': m.id,
                    'body': m.body,
                    'sender': m.sender,
                    'pub_date': m.pub_date
                }
            }
        else:
            raise NotFound

    def put(self, query_like):
        """
        from requests import put

        put(
            'http://localhost:5000/15',
            data={
                'sender': 's15',
                'body': 'bla 15'
            }
        )
        """
        b, s = [request.form[item] for item in ('body', 'sender')]
        m = Message(body=b, sender=s)
        sdb.session.add(m)
        sdb.session.commit()

        return {
            query_like: {
                'id': m.id,
                'body': b,
                'sender': s,
                'pub_date': m.pub_date
            }
        }


class SimpleList(Resource):
    def get(self):
        ms = MessageSchema(many=True)
        ma = Message.query.all()
        return ms.dump(ma)


api.add_resource(SimpleRest, '/<string:query_like>')
api.add_resource(SimpleList, '/all')


if __name__ == '__main__':
    app.run(debug=True)
