#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date : 2019/1/26 18:15
# Author : Me
import csv

from plotly import offline as off
from plotly import plotly
import plotly.graph_objs as go

off.init_notebook_mode(connected=True)

x = []
y = []
with open('province.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for item in reader:
        if item[0] != 'None':
            x.append(item[0])
            y.append(int(item[1]))

data = [go.Bar(x=x, y=y)]
layout = go.Layout(title='酷安地区分布',titlefont={'size':25},yaxis={'title':'人数'})
layout.annotations=[{'text':'未设置地区人数：395916','showarrow':False,'x':34,'y':11000}]

fig = {'data': data, 'layout': layout}

off.plot(fig, filename='province.html', auto_open=True)
# plotly.offline.iplot({
#     "data": [go.Scatter(x=[1, 2, 3, 4], y=[4, 3, 2, 1])],
#     "layout": go.Layout(title="hello world")
# })
