#!/usr/bin/env python3
# -*- coding: utf-8 -*-

# __author__ = 'kira@-天底 ガジ'

from config import time_config as tc
from datetime import datetime


def time_format():
    date = datetime.utcnow()

    return tc.TIME_TEMPLATE.format(
        date, tc.DAYS[date.weekday()]
    )
