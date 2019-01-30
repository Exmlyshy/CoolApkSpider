#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date : 2019-01-24 10:55:43
import os
import time
from datetime import datetime


def time2format(t):
    return datetime.fromtimestamp(t).strftime('%Y%m%d.%H%M%S')

def get_time2token(start,expire):
    temp = start
    while temp <= expire:
        cmd_time = time2format(temp)
        print('cmd time:%s' % cmd_time)
        cmd_SetTime = 'adb shell date -s %s' % cmd_time
        os.system(cmd_SetTime)
        time.sleep(1)
        cmd_TapScreen='adb shell input tap 360 800'
        os.system(cmd_TapScreen)
        temp += 6 * 60
        time.sleep(2)


if __name__ == '__main__':

    start_time = input('请输入开始时间(格式：2012-01-01 12:00:11):')
    max_age = input('请输入有效期（小时）：')
    start_timestamp = datetime.strptime(
        start_time, '%Y-%m-%d %H:%M:%S').timestamp()
    print('当前时间戳为:%s' % start_timestamp)
    expire_time = start_timestamp + float(max_age) * 60 * 60
    print('过期时间戳为:%s' % expire_time)
    get_time2token(start_timestamp,expire_time)

    
