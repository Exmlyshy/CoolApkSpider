#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date : 2019/1/27 14:22
# Author : Me
import csv

from plotly import offline as off
import plotly.graph_objs as go

off.init_notebook_mode(connected=True)

if __name__ == '__main__':
    with open('fans_top100.csv', 'r', encoding='utf-8') as f:
        reader = csv.reader(f)
        next(reader)
        users = list(reader)[:20]
    x, y = [], []
    for user in users:
        x.append(user[0])
        y.append(user[1])

    data = [go.Bar(x=x, y=y)]
    layout = go.Layout(title='酷安粉丝数top20')
    layout.title.font = {'size': 25}
    fig = {'data': data, 'layout': layout}

    off.plot(fig, filename='fans_top10.html', auto_open=True)
