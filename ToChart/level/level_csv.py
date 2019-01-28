#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date : 2019/1/26 19:13
# Author : Me
import csv
import pymongo

client = pymongo.MongoClient()
db = client['coolapk']
collection = db['user']

slice = ['0', '1', '2', '3', '4', '5', '6-10', '11-20', '21-40', '41-60']

def csv_write(fp, data):
    writer = csv.writer(fp)
    writer.writerow(['等级', '人数'])
    for k, v in data.items():
        writer.writerow(['level: '+k, v])
        print('write %s:%s' % (k, v))

if __name__ == '__main__':

    level_count = {}
    for item in slice[:6]:
        level = int(item)
        count = collection.count_documents({'level': level})
        print(item, count)
        level_count[item]=count

    for item in slice[6:]:
        min, max = int(item.split('-')[0]), int(item.split('-')[1])
        count = collection.count_documents({'level': {'$gte': min, '$lte': max}})
        print(item, count)
        level_count[item]=count

    filename = 'level.csv'
    fp = open(filename, 'w', newline='')
    csv_write(fp, level_count)
    client.close()
    fp.close()