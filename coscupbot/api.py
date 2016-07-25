# -*- coding: utf-8 -*-

from linebot.client import *
import logging


def check_result(result):
    if result.status_code is 200:
        return result
    raise ApiError('Api Error. %s' % result.content, result)


class LineApi(object):
    def __init__(self, credentials):
        self.client = LineBotClient(**credentials)
        self.logger = logging.getLogger('LineApi')

    def send_text(self, **args):
        self.logger.info("Bot api send message. %s" % args)
        return check_result(self.client.send_text(**args))


class ApiError(Exception):
    def __init__(self, message, request_result):
        super(ApiError, self).__init__(message)
        self.request_result = request_result
