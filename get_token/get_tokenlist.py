#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date : 2019-01-24 10:46:41
from datetime import datetime
from redis import StrictRedis
from config import *

redis = StrictRedis(REDISURI)


def request(flow):
    Request = flow.request
    localtime = datetime.strftime(datetime.now(), '%Y-%m-%d %H:%M:%S')
    print(Request.url)
    if 'api.coolapk' in Request.url:
        token = Request.headers.get('x-app-token')
        if token:
            print('%s : Get token:%s' % (localtime, token))
            redis.rpush('token', token)
        else:
            print('%s : Can Not Find x-app-token.' % localtime)
