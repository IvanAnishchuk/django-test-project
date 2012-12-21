# coding: utf-8
""" Logging middlewares """
import logging
import logging.handlers
from django.conf import settings
from django.db import connection
from decimal import Decimal

logger = logging.getLogger('sql_query_logger')


class SQLQueryLoggerMiddleware(object):
    """ Middleware logging all sql queries """
    def process_response(self, request, response):
        if connection.queries:
            logger.debug(
                '=== SQL log for {} ==='.format(
                    request.get_full_path()
                )
            )
            time = Decimal(0)
            for query in connection.queries:
                logger.debug('{sql} exec time {time} s.'.format(**query))
                time += Decimal(query['time'])
            logger.debug(
                '=== {} queries for {}, total time {} s. ==='.format(
                    len(connection.queries),
                    request.get_full_path(),
                    time,
                )
            )
        return response
