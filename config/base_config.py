#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-天底 ガジ'

from os import getcwd
from sys import platform
from os.path import join

from itertools import count


class BaseConfig:
    DEBUG = True
    SLASH = '/' * (3 if 'win' in platform else 4)

    SQLALCHEMY_DATABASE_URI = "sqlite:{}{}".format(
        SLASH, join(getcwd(), 'st.db')
    )

    SQLALCHEMY_TRACK_MODIFICATIONS = False


class AppConfig:
    # https://github.com/4m3s0k0/isshuukan_friends/blob/master/Kaori_.py
    DAYS = ['月曜日', '火曜日', '水曜日', '木曜日', '金曜日', '土曜日', '日曜日']
    DAYS = dict(zip(count(), DAYS))
    TIME_UPPERS = "{1}{0.year}年{0.month}月{0.day}日"
    TIME_LOWERS = "{0.hour}時{0.minute}分{0.second}秒"
    TIME_TEMPLATE = "/".join((TIME_UPPERS, TIME_LOWERS))
