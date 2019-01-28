#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date : 2019/1/28 10:20
# Author : Me

import csv
import pymongo

client = pymongo.MongoClient()
db = client['coolapk']
collection = db['user']

provinces = ['天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南',
             '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆', '台湾', '香港', '澳门', '北京', '海外'
             ]


def csv_write(fp, data):
    writer = csv.writer(fp)
    writer.writerow(['省份', '男', '女'])
    for item in data:
        writer.writerow(item)
        print('write %s'%item[0])


if __name__ == '__main__':
    gender_province = []
    for province in provinces:
        female = collection.count_documents({'province': province, 'gender': 0})
        male = collection.count_documents({'province': province, 'gender': 1})
        count = female + male
        gender_province.append(
            [province, '{:.2f}%'.format(male / count * 100), '{:.2f}%'.format(female / count * 100)])

    filename = 'gender_province.csv'
    fp = open(filename, 'w', newline='')
    csv_write(fp, gender_province)
    client.close()
    fp.close()
