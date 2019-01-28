#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date : 2019-01-26 14:23:02

import csv
import pymongo

provinces = ['天津', '河北', '山西', '内蒙古', '辽宁', '吉林', '黑龙江', '上海', '江苏', '浙江', '安徽', '福建', '江西', '山东', '河南', '湖北', '湖南',
             '广东', '广西', '海南', '重庆', '四川', '贵州', '云南', '西藏', '陕西', '甘肃', '青海', '宁夏', '新疆', '台湾', '香港', '澳门', '北京', '海外',
             'None']
client = pymongo.MongoClient()
db = client['coolapk']
collection = db['user']


def csv_write(fp, data):
    writer = csv.writer(fp)
    writer.writerow(['省份', '人数'])
    for k, v in data.items():
        writer.writerow([k, v])
        print('write %s:%s' % (k, v))


if __name__ == '__main__':

    province_names = collection.distinct('province')

    provinces_dict = {}
    for province in province_names:
        count = collection.count_documents({'province': province})
        print(province, count)
        provinces_dict[province] = count

    provinces_count = {}
    for province in provinces:
        provinces_count[province] = 0
        for name in provinces_dict.keys():
            if province is not '' and province in name:
                provinces_count[province] += provinces_dict[name]
    provinces_count['None'] = provinces_dict['']

    filename = 'province.csv'
    fp = open(filename, 'w', newline='')
    csv_write(fp, provinces_count)
    client.close()
    fp.close()
