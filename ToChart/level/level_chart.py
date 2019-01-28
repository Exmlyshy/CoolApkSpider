#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date : 2019/1/26 19:45
# Author : Me
import csv

from plotly import offline as off
import plotly.graph_objs as go

off.init_notebook_mode(connected=True)

labels = []
values = []
with open('level.csv', 'r') as f:
    reader = csv.reader(f)
    next(reader)
    for item in reader:
        labels.append(item[0])
        values.append(int(item[1]))

data = [go.Pie(labels=labels, values=values, textinfo='label+percent')]

layout = go.Layout(title='酷安等级分布')
layout.title.font={'size':25}

fig = {'data': data, 'layout': layout}
off.plot(fig, filename='level.html', auto_open=True)
