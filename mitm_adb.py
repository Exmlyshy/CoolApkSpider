#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date    : 2019-01-21 16:40:31
'''
使用多进程管理爬虫依赖项

'''
from adb import refresh
import time
from multiprocessing import Pool
import subprocess
import os


def run_mitmdump():
    path = os.path.join(os.path.abspath('.'), 'mitm_token')
    cmd = 'mitmdump -s gettoken.py'
    subprocess.call(cmd, shell=True, cwd=path)


def run_adb():
    refresh.main()


def clean_screen():
    for i in range(20):
        time.sleep(60 * 60)
        os.system('cls')



if __name__ == '__main__':
    p = Pool(3)
    tasks = [run_mitmdump, run_adb, clean_screen]
    for task in tasks:
        p.apply_async(task)
    p.close()
    p.join()
