#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-天底 ガジ'

from os import getcwd
from sys import platform
from os.path import join


class BaseConfig:
    DEBUG = True
    SLASH = '/' * (3 if 'win' in platform else 4)

    SQLALCHEMY_DATABASE_URI = "sqlite:{}{}".format(
        SLASH, join(getcwd(), 'st.db')
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False
