#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date : 2019/1/27 13:09
# Author : Me
import csv
import pymongo
from plotly import offline as off
import plotly.graph_objs as go

off.init_notebook_mode(connected=True)

client = pymongo.MongoClient()
db = client['coolapk']
collection = db['user']

if __name__ == '__main__':
    female = collection.count_documents({'gender': 0})
    male = collection.count_documents({'gender': 1})
    male_and_female = collection.count_documents({'gender': -1})

    data = [go.Pie(labels=['女', '男', '其他'], values=[female, male, male_and_female], textinfo='label+percent')]
    layout = go.Layout(title='酷安性别分布')
    layout.title.font = {'size': 25}
    fig = {'data': data, 'layout': layout}
    off.plot(fig, filename='gender.html', auto_open=True)
    client.close()

