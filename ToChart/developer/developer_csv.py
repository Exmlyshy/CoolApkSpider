#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date : 2019/1/27 13:52
# Author : Me
import csv
import pymongo

client = pymongo.MongoClient()
db = client['coolapk']
collection = db['user']


def csv_write(fp, data):
    writer = csv.writer(fp)
    writer.writerow(['用户名', '应用数', '排名'])
    for i, item in enumerate(data, start=1):
        writer.writerow([item.get('username'), item.get('apkDevNum'), i])
        print('write %s'%item.get('username'))


if __name__ == '__main__':
    developers = collection.find({'isDeveloper': 1}).sort('apkDevNum', pymongo.DESCENDING)[:250]

    filename = 'developer.csv'
    fp = open(filename, 'w', newline='')
    csv_write(fp, developers)
    client.close()
    fp.close()
