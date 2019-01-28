# -*- coding: utf-8 -*-
import json
import os
import time

import scrapy
from scrapy.exceptions import CloseSpider

from coolapkuser.items import UserItem


class CoolapkSpider(scrapy.Spider):
    name = 'coolapk'
    allowed_domains = ['coolapk.com']
    start_urls = ['http://coolapk.com/']
    error_count = 0
    time_flag = time.time()

    start_uid = 12202
    start_url = 'https://api.coolapk.com/v6/user/space?uid=12202'
    user_url = 'https://api.coolapk.com/v6/user/space?uid={uid}'
    feed_url = 'https://api.coolapk.com/v6/user/feedlist?uid={uid}&page={page}'
    fans_url = 'https://api.coolapk.com/v6/user/fanslist?uid={uid}&page={page}'
    # firstitem是关注的第一个用户uid,lastitem是前一页最后一个用户uid
    follow_url = 'https://api.coolapk.com/v6/user/followlist?uid={uid}&page={page}'

    def start_requests(self):
        user_url = self.user_url.format(uid=self.start_uid)
        yield scrapy.Request(user_url, callback=self.parse_user)

    def parse_user(self, response):

        if time.time() - self.time_flag > 60:
            os.system('cls')
            self.time_flag = time.time()

        item = UserItem()
        try:
            data = json.loads(response.body)
            if isinstance(data, dict):
                userdata = data.get('data')
                if isinstance(userdata, dict):
                    for field in item.fields:
                        if field in userdata:
                            item[field] = userdata.get(field)
                    yield item
            follow=item.get('follow')
            if follow:
                for page in range(int(item.get('follow')) // 20 + 1):
                    yield scrapy.Request(self.follow_url.format(uid=item.get('uid'), page=page + 1),
                                         callback=self.parse_follows)
                    time.sleep(0.01)
            fans=item.get('fans')
            if fans:
                for page in range(int(item.get('fans')) // 20 + 1):
                    yield scrapy.Request(self.fans_url.format(uid=item.get('uid'), page=page + 1), callback=self.parse_fans)
                    time.sleep(0.01)
        

        except json.decoder.JSONDecodeError:
            self.logger.warning('json decode error.')

    def parse_follows(self, response):
        try:
            data = json.loads(response.body)
            if isinstance(data, dict):
                user_list = data.get('data')
                if isinstance(user_list, list):
                    for user in user_list:
                        if user.get('fuid'):
                            yield scrapy.Request(self.user_url.format(uid=user.get('fuid')), callback=self.parse_user)

        except json.decoder.JSONDecodeError:
            self.logger.warning('json decode error.')

    def parse_fans(self, response):
        try:
            data = json.loads(response.body)
            if isinstance(data, dict):
                user_list = data.get('data')
                if isinstance(user_list, list):
                    for user in user_list:
                        if user.get('uid'):
                            yield scrapy.Request(self.user_url.format(uid=user.get('uid')), callback=self.parse_user)

        except json.decoder.JSONDecodeError:
            self.logger.warning('json decode error.')
