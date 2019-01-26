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

    token_list: list

    def __init__(self, token_list):
        self.logger = logging.getLogger(__name__)
        # self.db = StrictRedis(redis_uri)
        self.token_list=token_list

    @classmethod
    def from_crawler(cls, crawler):
        redis=StrictRedis(crawler.settings.get('REDIS_URI'))
        try:
            token_list = redis.lrange('token', 0, redis.llen('token'))
        except Exception as e:
            raise e

        return cls(
            token_list
        )

    def _get_token(self,token_list):
        for token in token_list:
            token_time = token[-10:].decode('utf-8')
            if abs(time.time() - int(token_time, base=16)) < 4 * 60:
                return token.decode('utf-8')

    def process_request(self, request, spider):
        token = self._get_token(self.token_list)
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
                token = self._get_token(self.token_list)
                if token:
                    self.logger.info('Get token:%s' % token)
                    request.headers['x-app-token'] = token
                else:
                    self.logger.warning('Get token failed.')

            except Exception as e:
                self.logger.error(e)

            return request

        return response
