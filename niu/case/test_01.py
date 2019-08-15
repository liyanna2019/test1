# -*- coding: utf-8 -*-
import requests
import unittest
from common.login import Login




class Test(unittest.TestCase):
    def setUp(self):
        print('测试开始')

    def tearDown(self):
        print('测试结束')

    def test_login(self):
        result = Login().niu_login()
        print(result)
        self.assertEqual(result['code'], 0)







