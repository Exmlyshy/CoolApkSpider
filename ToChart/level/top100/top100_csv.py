#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date : 2019/1/27 10:24
# Author : Me
import csv
import pymongo

client = pymongo.MongoClient()
db = client['coolapk']
collection = db['user']


def csv_write(fp, data):
    writer = csv.writer(fp)
    writer.writerow(['用户名', '等级', '排名'])
    for user in data:
        writer.writerow(user)
        print('write to csv:%s' % user[0])


if __name__ == '__main__':
    top100_obj = collection.find({'level': {'$gt': 30}}).sort('level', pymongo.DESCENDING)[:100]
    top100 = []
    for i, item in enumerate(top100_obj, start=1):
        user = (item.get('username'), item.get('level'), i)
        top100.append(user)

    filename = 'top100.csv'
    fp = open(filename, 'w', newline='')
    csv_write(fp, top100)
    client.close()
    fp.close()

