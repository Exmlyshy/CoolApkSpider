# -*- coding: utf-8 -*-

# Define here the models for your spider middleware
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/spider-middleware.html
import logging
import os
import time

from redis import StrictRedis
from scrapy.exceptions import IgnoreRequest


class CloseMiddlerWare(object):
    '''
        0 : signal.CTRL_C_EVENT
        1 : signal.CTRL_BREAK_EVENT
    '''

    def process_request(self, request, spider):
        if spider.error_count > 10:
            os.kill(os.getpid(), 0)


class TokenMiddleware(object):

    def __init__(self, redis_uri):
        self.logger = logging.getLogger(__name__)
        self.db = StrictRedis(redis_uri)

    @classmethod
    def from_crawler(cls, crawler):
        return cls(
            crawler.settings.get('REDIS_URI'),
        )

    def _get_token(self):
        token = self.db.get('token')
        return token

    def process_request(self, request, spider):
        token = self._get_token()
        if token:
            self.logger.info('Get token:%s' % token)
            request.headers['x-app-token'] = token
        else:
            self.logger.warning('Get token failed.')
            spider.error_count += 1
            time.sleep(2)
            return request

    def process_response(self, request, response, spider):
        if response.status >= 400:
            self.logger.warning('GET %s failed.' % request.url)
            spider.error_count += 1
            time.sleep(2)
            try:
                token = self._get_token()
                if token:
                    self.logger.info('Get token:%s' % token)
                    request.headers['x-app-token'] = token
                else:
                    self.logger.warning('Get token failed.')

            except Exception as e:
                self.logger.error(e)

            return request

        return response
