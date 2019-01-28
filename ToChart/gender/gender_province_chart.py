#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date : 2019/1/28 10:41
# Author : Me
import csv
from plotly import offline as off
import plotly.graph_objs as go

off.init_notebook_mode(connected=True)

if __name__ == '__main__':
    province = []
    male = []
    female = []
    with open('gender_province.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        for item in reader:
            province.append(item[0])
            male.append(item[1])
            female.append(item[2])

    trace0 = go.Bar(x=province, y=male, name='男')
    trace1 = go.Bar(x=province, y=female, name='女')
    data = [trace0, trace1]
    layout = go.Layout(title='酷安性别-地区分布', titlefont={'size': 25}, yaxis={'title': '占比'})
    fig = {'data': data, 'layout': layout}

    off.plot(fig, filename='gender_province.html', auto_open=True)
