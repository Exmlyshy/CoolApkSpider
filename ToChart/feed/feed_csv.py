#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date : 2019/1/28 9:31
# Author : Me
import pymongo
import csv

client = pymongo.MongoClient()
db = client['coolapk']
collection = db['user']


def csv_write(fp,data):
    writer=csv.writer(fp)
    writer.writerow(['用户名','动态数','排名'])
    for i, item in enumerate(data, start=1):
        writer.writerow([item.get('username'), item.get('feed'), i])
        print('write %s' % item.get('username'))

if __name__ == '__main__':

    users=collection.find().sort('feed',pymongo.DESCENDING).limit(100)
    filename = 'fans_top100.csv'
    fp = open(filename, 'w', encoding='utf-8', newline='')
    csv_write(fp, users)
    client.close()
    fp.close()