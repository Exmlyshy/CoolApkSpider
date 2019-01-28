#!/usr/bin/env python
# -*- coding: utf-8 -*-
# Date : 2019/1/27 10:58
# Author : Me
import csv

from plotly import offline as off
import plotly.graph_objs as go

off.init_notebook_mode(connected=True)


def to_chart(x, y, z=None, title=None):
    data = [go.Bar(x=x, y=y, orientation='h', text=z)]
    layout = go.Layout(title=title)
    layout.title.font = {'size': 25}
    fig = go.Figure(data=data, layout=layout)

    off.plot(fig, filename='{title}.html'.format(title=title), auto_open=True)


def to_chart_(users, start=None, end=None, title=None):
    x, y, z = [], [], []

    for item in users[start - 1:end][::-1]:
        print(item[0], ':', item[1])
        y.append(item[0])
        x.append(int(item[1]))
        z.append('rank {}'.format(item[2]))
    to_chart(x, y, z, title=title)


if __name__ == '__main__':
    with open('top100.csv', 'r') as f:
        reader = csv.reader(f)
        next(reader)
        users = list(reader)
    to_chart_(users, 51, 100, title='酷安等级top51-100')
    to_chart_(users, 26, 50, title='酷安等级top26-50')
    to_chart_(users, 1, 25, title='酷安等级top1-25')
    # x = []
    # y = []
    # z = []
    # with open('top100.csv', 'r') as f:
    #     reader = csv.reader(f)
    #     next(reader)
    #     users = list(reader)
    #     for item in users[:50:-1]:
    #         print(item[0], ':', item[1])
    #         y.append(item[0])
    #         x.append(int(item[1]))
    #         z.append('rank {}'.format(item[2]))
    #     to_chart(x, y, z, title='酷安等级top51-100')
    #
    #     x.clear()
    #     y.clear()
    #     z.clear()
    #     for item in users[50:25:-1]:
    #         print(item[0], ':', item[1])
    #         y.append(item[0])
    #         x.append(int(item[1]))
    #         z.append('rank {}'.format(item[2]))
    #     to_chart(x, y, z, title='酷安等级top25-50')

    #
