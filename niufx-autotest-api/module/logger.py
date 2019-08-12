#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date       : 2019-07-08 15:03:41
# @Author     : caryangBingo
# @Filename   : logger.py
# @Version    : Version 1.0

import io
import os
import sys
import time
import logging


_base_dir = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
_base_dir = _base_dir.replace('\\', '/')

LEVELS = {
    'debug': logging.DEBUG,
    'info': logging.INFO,
    'warning': logging.WARNING,
    'error': logging.ERROR,
    'critical': logging.CRITICAL
}

logger = logging.getLogger()
level = 'default'


def create_file(filename):
    path = filename[0:filename.rfind('/')]
    if not os.path.isdir(path):
        os.makedirs(path)
    if not os.path.isfile(filename):
        fd = open(filename, mode='w', encoding='utf-8')
        fd.close()
    else:
        pass


def set_handler(levels):
    if levels == 'error':
        logger.addHandler(Logging.err_handler)
    logger.addHandler(Logging.handler)


def remove_handler(levels):
    if levels == 'error':
        logger.removeHandler(Logging.err_handler)
    logger.removeHandler(Logging.handler)


def get_current_time():
    return time.strftime(Logging.date, time.localtime(time.time()))


class Logging:
    #path = os.path.dirname(os.path.dirname(os.path.abspath(__file__)))
    log_file = _base_dir + '/resource/log/log.log'
    err_file = _base_dir + '/resource/log/err.log'
    logger.setLevel(LEVELS.get(level, logging.NOTSET))
    create_file(log_file)
    create_file(err_file)
    date = '%Y-%m-%d %H:%M:%S'

    handler = logging.FileHandler(log_file, encoding='utf-8')
    err_handler = logging.FileHandler(err_file, encoding='utf-8')

    @staticmethod
    def debug(log_meg):
        set_handler('debug')
        logger.debug("[DEBUG " + get_current_time() + "]" + log_meg)
        remove_handler('debug')

    @staticmethod
    def info(log_meg):
        set_handler('info')
        logger.info("[INFO " + get_current_time() + "]" + log_meg)
        remove_handler('info')

    @staticmethod
    def warning(log_meg):
        set_handler('warning')
        logger.warning("[WARNING " + get_current_time() + "]" + log_meg)
        remove_handler('warning')

    @staticmethod
    def error(log_meg):
        set_handler('error')
        logger.error("[ERROR " + get_current_time() + "]" + log_meg)
        remove_handler('error')

    @staticmethod
    def critical(log_meg):
        set_handler('critical')
        logger.error("[CRITICAL " + get_current_time() + "]" + log_meg)
        remove_handler('critical')


if __name__ == "__main__":
    Logging.debug("This is debug message")
    Logging.info("This is info message")
    Logging.warning("This is warning message")
    Logging.error("This is error")
    Logging.critical("This is critical message")
