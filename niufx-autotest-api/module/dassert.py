#!/usr/bin/python3
# -*- coding: utf-8 -*-
# @Date       : 2019-07-04 19:55:55
# @Author     : caryangBingo
# @Filename   : dassert.py
# @Version    : Version 1.0

import io
import os
import re
import sys
import json
import pysnooper
from module import logger
sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')


class Assertions(object):
    """docstring for Assertions"""

    def __init__(self):
        self.logger = logger.Logging()

    def assert_code(self, code, expected_code):
        """
        验证response状态码
        :param code:
        :param expected_code:
        :return:
        """
        try:
            assert code == expected_code
            return True
        except:
            self.logger.error("statusCode error, expected_code is %s, statusCode is %s " % (
                expected_code, code))
            raise

    def assert_msg(self, msg, expected_msg):
        """
        验证response message中任意属性的值
        :param msg:
        :param expected_msg:
        :return:
        """
        try:
            assert msg == expected_msg
            return True
        except:
            self.logger.error("Response msg != expected_msg, expected_msg is %s, msg is %s" % (
                expected_msg, msg))
            raise

    def assert_body(self, body, expected_body):
        """
        验证response body中任意属性的值
        :param body:
        :param expected_body:
        :return:
        """
        try:
            assert body == expected_body
            return True
        except AssertionError:
            print('>>>返回结果中与预期不同：\n\n')
            Assertions.assert_diff(self, json.loads(
                str(body)), json.loads(str(expected_body)))
            return False
        except:
            self.logger.error("Response body != expected_body, expected_body is %s, body is %s" % (
                expected_body, body))
            raise

    def assert_regex(self, text, expected_regex):
        """
        验证response body中是否正则匹配预期字符串
        :param text:
        :param expected_regex:
        :return:
        """
        try:
            expected_regex = re.compile(expected_regex)
            assert expected_regex.findall(text)
            return True
        except:
            self.logger.error(
                "Response text Does not regular expected_regex, Response text is %s " % text)
            raise

    def assert_in_text(self, text, expected_text):
        """
        验证response body中是否包含预期字符串
        :param text:
        :param expected_text:
        :return:
        """
        try:
            text = json.dumps(text, ensure_ascii=False)
            assert expected_text in text
            return True
        except:
            self.log.error(
                "Response body Does not contain expected_text, expected_text is %s" % expected_text)
            raise

    def assert_subCode(self, subCode, expected_subCode):
        """
        验证response subCode中任意属性的值
        :param subCode:
        :param expected_subCode:
        :return:
        """
        try:
            assert subCode == expected_subCode
            return True
        except:
            self.logger.error("Response subCode != expected_subCode, expected_subCode is %s, subCode is %s" % (
                expected_subCode, subCode))
            raise

    def assert_time(self, time, expected_time):
        """
        验证response body响应时间小于预期最大响应时间,单位：毫秒
        :param body:
        :param expected_time:
        :return:
        """
        try:
            assert time < expected_time
            return True
        except:
            self.log.error("Response time > expected_time, expected_time is %s, time is %s" % (
                expected_time, time))
            raise

    def assert_diff(self, A, B, xpath='.'):
        if isinstance(A, list) and isinstance(B, list):
            for i in range(len(A)):
                try:
                    Assertions.assert_diff(self,
                                           A[i], B[i], xpath + '[%s]' % str(i))
                except:
                    print('>>> A.[实际结果]中的%s[%s]未在[预期结果]中找\n' % (xpath, i))
        if isinstance(A, dict) and isinstance(B, dict):
            for i in A:
                try:
                    B[i]
                except:
                    print('>>> B.实际结果中的%s/%s 未在预期结果中找到\n' % (xpath, i))
                    continue
                if not (isinstance(A.get(i), (list, dict)) or isinstance(B.get(i), (list, dict))):
                    if type(A.get(i)) != type(B.get(i)):
                        print('>>> C.类型不同参数在[实际结果]中的绝对路径:  %s/%s  ►►► 实际结果 = %s, 预期结果 = %s \n' %
                              (xpath, i, type(A.get(i)), type(B.get(i))))
                    elif A.get(i) != B.get(i):
                        print(
                            '>>> D.内容不同参数在[实际结果]中的绝对路径: {0}/{1}  ►►► 实际结果 = {2} , 预期结果 = {3} \n\n'.format(xpath, i, A.get(i), B.get(i)))
                    continue
                Assertions.assert_diff(
                    self, A.get(i), B.get(i), xpath + '/' + str(i))
            return
        if type(A) != type(B):
            print('>>> E.类型不同参数在[实际结果]中的绝对路径:  %s  ►►► 实际结果 = %s, 预期结果 = %s \n' % (
                xpath, type(A), type(B)))
        elif A != B and type(A) is not list:
            print('>>> F.内容不同参数在[实际结果]中的绝对路径:  %s  ►►► 实际结果 = %s, 预期结果 = %s \n' % (
                xpath, A, B))
