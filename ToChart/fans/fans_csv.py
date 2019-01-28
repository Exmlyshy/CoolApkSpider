#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date : 2019/1/27 14:14
# Author : Me
import csv
import pymongo

client = pymongo.MongoClient()
db = client['coolapk']
collection = db['user']


def csv_write(fp, data):
    writer = csv.writer(fp)
    writer.writerow(['用户名', '粉丝数', '排名'])
    for i, item in enumerate(data, start=1):
        writer.writerow([item.get('username'), item.get('fans'), i])
        print('write %s' % item.get('username'))


if __name__ == '__main__':
    fans_top100 = collection.find().sort('fans', pymongo.DESCENDING).limit(100)

    filename = 'fans_top100.csv'
    fp = open(filename, 'w', encoding='utf-8', newline='')
    csv_write(fp, fans_top100)
    client.close()
    fp.close()
