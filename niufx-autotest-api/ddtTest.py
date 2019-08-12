#!/usr/bin/env python
# -*- coding: utf-8 -*-
# @Date       : 2019-04-30 09:43:54
# @Author     : caryangBingo
# @Filename   : ddtTest.py
# @Version    : Version 1.0

import io
import os
import sys
import requests
import unittest
from config.config_docs import getConfig
from module.ddt import ddt, file_data
from module.dassert import Assertions
from module.BeautifulReport import BeautifulReport

#sys.stdout = io.TextIOWrapper(sys.stdout.buffer, encoding='utf-8')

baseUrl = getConfig("niufxPath_test", "baseUrl")

Assertions = Assertions()


@ddt
class Get_InterfaceTest(unittest.TestCase):

    def setUp(self):
        self.niufx_url = '{}'.format(baseUrl)

    def tearDown(self):
        print(self.reqUrl)
        print(self.result)

    """
    # 获取指定用户申诉账号进度信息
    @file_data("./data/testData/AccountAppealController/getAccountsByAppealUidUsingGET_1.json")
    def test_api_getAccountsByAppealUid_request(self, appealUid, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.coinMall_url +
                         '/api/getAccountsByAppealUid', params={"appealUid": appealUid})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)
    """

    # 检查用户是否和账户匹配
    @file_data("./data/testData/AccountInfoController/checkAccountByIdUsingGET_7.yaml")
    def test_api_checkAccountById_request(self, accountId, uid, currentUid, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/checkAccountById', params={"accountId": accountId, "uid": uid, "currentUid": currentUid})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    # 获取指定交易账户信息(用于修改账户信息时获取账户详细信息)
    @file_data("./data/testData/AccountInfoController/getAccountByIdUsingGET_7.yaml")
    def test_api_getAccountById_request(self, accountId, uid, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getAccountById', params={"accountId": accountId, "uid": uid})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    # 查询账户信息列表
    @file_data("./data/testData/AccountInfoController/getAccountListUsingGET.yaml")
    def test_api_getAccountList_request(self, uid, accountStatus, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getAccountList', params={"uid": uid, "accountStatus": accountStatus})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    # 查询指定用户发送红包的状态
    @file_data("./data/testData/AccountInfoController/getBindingSituationByUidUsingGET_1.yaml")
    def test_api_getBindingSituationByUid_request(self, uid, versions, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getBindingSituationByUid', params={"uid": uid, "versions": versions})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    # 获取指定类型热搜词列表
    @file_data("./data/testData/AccountInfoController/getHotSearchWordsByTypeUsingGET_1.yaml")
    def test_api_getHotSearchWordsByType_request(self, searchType, topSize, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getHotSearchWordsByType', params={"searchType": searchType, "topSize": topSize})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    # 获得杠杆比例列表
    @file_data("./data/testData/AccountInfoController/getLeverUsingGET_1.yaml")
    def test_api_getLever_request(self, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getLever', params=None)
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    # 获得账户权限字典信息(添加账户时需要调用)
    @file_data("./data/testData/AccountInfoController/getPermissionsUsingGET_1.yaml")
    def test_api_getPermissions_request(self, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getPermissions', params=None)
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    # 获得账户权限字典信息(添加账户时需要调用)
    @file_data("./data/testData/AccountInfoController/getPositionOrderPageUsingGET_1.yaml")
    def test_api_getPositionOrderPage_request(self, accountId, snapTimeTicks, pageIndex, pageSize, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getPositionOrderPage', params={"accountId": accountId, "snapTimeTicks": snapTimeTicks, "pageIndex": pageIndex, "pageSize": pageSize})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    # 今日盈亏分享
    @file_data("./data/testData/AccountInfoController/getProfitShareByIdUsingGET.yaml")
    def test_api_getProfitShareById_request(self, accountId, uid, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getProfitShareById', params={"accountId": accountId, "uid": uid})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    # 获取指定用户真实交易账户统计信息
    @file_data("./data/testData/AccountInfoController/getRealStatisTinysUsingGET_1.yaml")
    def test_api_getRealStatisTinys_request(self, uid, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getRealStatisTinys', params={"uid": uid})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    # 获取用户关键字匹配的所有账号排行统计信息
    @file_data("./data/testData/AccountInfoController/getStatisPageByUidsUsingGET_1.yaml")
    def test_api_getStatisPageByUids_request(self, userKeyWord, uid, accountType, pageIndex, pageSize, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getStatisPageByUids', params={"userKeyWord": userKeyWord, "uid": uid, "accountType": accountType, "pageIndex": pageIndex, "pageSize": pageSize})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    # 获取用户总交易统计信息
    @file_data("./data/testData/AccountInfoController/getTotalStatisByUidUsingGET.yaml")
    def test_api_getTotalStatisByUid_request(self, uid, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getTotalStatisByUid', params={"uid": uid})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    # 获取新晋交易用户
    @file_data("./data/testData/AccountInfoController/getUserNewUsingGET.yaml")
    def test_api_getUserNew_request(self, topSize, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getUserNew', params={"topSize": topSize})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    # 查询指定用户ID、交易账户经纪商关联ID集合信息
    @file_data("./data/testData/AccountInfoForYunpcAndZhuzController/getAccountRelBrokerIdsByUidUsingGET_7.yaml")
    def test_api_getAccountRelBrokerIdsByUid_request(self, uid, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getAccountRelBrokerIdsByUid', params={"uid": uid})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    # 查询指定用户ID、交易账户经纪商关联集合信息
    @file_data("./data/testData/AccountInfoForYunpcAndZhuzController/getAccountsRelBrokerByUidUsingGET_15.yaml")
    def test_api_getAccountsRelBrokerByUid_request(self, uid, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getAccountsRelBrokerByUid', params={"uid": uid})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    """
    # 账号点赞/取消点赞
    @file_data("./data/testData/AccountPraiseController/getAccountPraiseApiUsingGET.yaml")
    def test_api_getAccountPraiseApi_request(self, accountId, type, uid, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getAccountPraiseApi', params={"accountId": accountId, "type": type, "uid": uid})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)
    """

    # 根据账户ID判断账户是否可浏览,(在进入用户详情前调用)
    @file_data("./data/testData/AccountTradeInfoController/getAccountStatusUsingGET_1.yaml")
    def test_api_getAccountStatus_request(self, uid, accountId, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getAccountStatus', params={"uid": uid, "accountId": accountId})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    # 获取指定交易账户详细交易信息(用户详情的上面部分)
    @file_data("./data/testData/AccountTradeInfoController/getAccountTradeDetailUsingGET.yaml")
    def test_api_getAccountTradeDetail_request(self, statisType, subscribeAccountId, subscribeUid, uid, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getAccountTradeDetail', params={"statisType": statisType, "subscribeAccountId": subscribeAccountId, "subscribeUid": subscribeUid, "uid": uid})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    # 获取指定交易账户详细交易信息实时数据信息(用户详情里的实时变化数据)
    @file_data("./data/testData/AccountTradeInfoController/getAccountTradeRealTimeDataUsingGET_1.yaml")
    def test_api_getAccountTradeRealTimeData_request(self, accountId, uid, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getAccountTradeRealTimeData', params={"accountId": accountId, "uid": uid})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    # 获取所有经纪商排名列表
    @file_data("./data/testData/AccountTradeInfoController/getBrokerRankUsingGET_1.yaml")
    def test_api_getBrokerRank_request(self, topSize, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getBrokerRank', params={"topSize": topSize})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    # 根据指定多个订单号获取交易订单通知详情
    @file_data("./data/testData/AccountTradeInfoController/getOrderLogByTicketsUsingGET_1.yaml")
    def test_api_getOrderLogByTickets_request(self, tickets, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getOrderLogByTickets', params={"tickets": tickets})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    # 获取指定交易账户订单列表分页内容（当前持仓、历史订单）
    @file_data("./data/testData/AccountTradeInfoController/getOrderPageUsingGET_1.yaml")
    def test_api_getOrderPage_request(self, accountId, ticketType, pageIndex, pageSize, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getOrderPage', params={"accountId": accountId, "ticketType": ticketType, "pageIndex": pageIndex, "pageSize": pageSize})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    """
    # 获取指定交易账户图形报表信息(用户详情下面的图形总收益、月收益)
    @file_data("./data/testData/AccountTradeInfoController/getOverviewListByAidUsingGET.yaml")
    def test_api_getOverviewListByAid_request(self, accountId, ticketType, pageIndex, pageSize, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getOverviewListByAid', params={"accountId": accountId, "ticketType": ticketType, "pageIndex": pageIndex, "pageSize": pageSize})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)
    """

    # 获取指定账号ID集合，对应账户简易信息集合
    @file_data("./data/testData/AccountTradeInfoController/getSmallAccountByIdsUsingGET_1.yaml")
    def test_api_getSmallAccountByIds_request(self, accountIds, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getSmallAccountByIds', params={"accountIds": accountIds})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    # 获取用户所有账户交易统计信息(查看别人或查看自己牛人榜账户交易信息)
    @file_data("./data/testData/AccountTradeInfoController/getStatisByUidUsingGET_1.yaml")
    def test_api_getStatisByUid_request(self, uid, currentUid, statisType, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getStatisByUid', params={"uid": uid, "currentUid": currentUid, "statisType": statisType})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    # 返回CODE代码查询，移动端调用时查询
    @file_data("./data/testData/ApiHelp/queryApiCodeUsingGET_1.yaml")
    def test_api_queryApiCode_request(self, http_statusCode, response):
        r = requests.get(self.niufx_url +
                         '/api/queryApiCode', params=None)
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        # self.assertEqual(self.result['code'], recode)
        # self.assertEqual(self.result['bodyMessage'], bodyMessage)
        # self.assertEqual(self.result['subCode'], subCode)
        self.assertEqual(self.result, response)

    # 返回CODE代码查询，服务端调用时查询
    @file_data("./data/testData/ApiHelp/queryServerCodeUsingGET_1.yaml")
    def test_api_queryServerCode_request(self, http_statusCode, response):
        r = requests.get(self.niufx_url +
                         '/api/queryServerCode', params=None)
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        # self.assertEqual(self.result['code'], recode)
        # self.assertEqual(self.result['bodyMessage'], bodyMessage)
        # self.assertEqual(self.result['subCode'], subCode)
        self.assertEqual(self.result, response)

    # 获取指定账号ID集合，对应账户简易信息集合
    @file_data("./data/testData/BrokerInfoController/getBrokerListUsingGET_1.yaml")
    def test_api_getBrokerList_request(self, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getBrokerList', params=None)
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    # 根据经济商ID查询所有该经济商服务器列表
    @file_data("./data/testData/BrokerInfoController/getBrokerServerListUsingGET_1.yaml")
    def test_api_getBrokerServerList_request(self, id, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getBrokerServerList', params={"id": id})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    # 根据主题获取评论分页
    @file_data("./data/testData/CommentReplyController/getCommentPagedUsingGET.yaml")
    def test_api_getCommentPaged_request(self, aboutId, currentUid, pageIndex, pageSize, returnReply, returnReplyCount, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getCommentPaged', params={"aboutId": aboutId, "currentUid": currentUid, "pageIndex": pageIndex, "pageSize": pageSize, "returnReply": returnReply, "returnReplyCount": returnReplyCount})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    # 根据评论ID获取跟评分页
    @file_data("./data/testData/CommentReplyController/getReplyPagedUsingGET_1.yaml")
    def test_api_getReplyPaged_request(self, aboutId, currentUid, pageIndex, pageSize, returnReply, returnReplyCount, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getReplyPaged', params={"aboutId": aboutId, "currentUid": currentUid, "pageIndex": pageIndex, "pageSize": pageSize, "returnReply": returnReply, "returnReplyCount": returnReplyCount})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    # 根据commentID点赞评论
    @file_data("./data/testData/CommentReplyController/praiseCommentUsingGET.yaml")
    def test_api_praiseComment_request(self, commentId, uid, type, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/praiseComment', params={"commentId": commentId, "uid": uid, "type": type})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    # 根据账户ID获取该账户的所有可订阅的品种及订阅价格
    @file_data("./data/testData/SubscribeController/getSymbolsByAccountUsingGET_1.yaml")
    def test_api_getSymbolsByAccount_request(self, uid, accountId, subscribeUid, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getSymbolsByAccount', params={"uid": uid, "accountId": accountId, "subscribeUid": subscribeUid})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)
    """
    # 牛人榜排行分页,同时提供排行榜搜索功能
    @file_data("./data/testData/SubscribeController/getTradeRankPageUsingGET.yaml")
    def test_api_getTradeRankPage_request(self, uid, accountId, subscribeUid, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/getTradeRankPage', params={"uid": uid, "accountId": accountId, "subscribeUid": subscribeUid})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)
    """

    # 查询我的普通订阅
    @file_data("./data/testData/SubscribeController/queryMySubscriptionUsingGET_1.yaml")
    def test_api_queryMySubscription_request(self, uid, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/queryMySubscription', params={"uid": uid})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    # 根据用户ID查询订阅粉丝
    @file_data("./data/testData/SubscribeController/queryUserFansUsingGET_1.yaml")
    def test_api_queryUserFans_request(self, uid, pageIndex, pageSize, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/queryUserFans', params={"uid": uid, "pageIndex": pageIndex, "pageSize": pageSize})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)

    # 取消订阅
    @file_data("./data/testData/SubscribeController/unSubscribeUsingGET.yaml")
    def test_api_unSubscribe_request(self, uid, accountId, symbol, unsubscribeUid, http_statusCode, recode, bodyMessage, subCode):
        r = requests.get(self.niufx_url +
                         '/api/unSubscribe', params={"uid": uid, "accountId": accountId, "symbol": symbol, "unSubscribe": unSubscribe})
        self.reqUrl = r.url
        self.result = r.json()
        self.assertEqual(r.status_code, http_statusCode)
        self.assertEqual(self.result['code'], recode)
        self.assertEqual(self.result['bodyMessage'], bodyMessage)
        self.assertEqual(self.result['subCode'], subCode)


if __name__ == '__main__':
    # unittest.main(verbosity=2)
    test_suite = unittest.TestSuite()
    test_suite.addTest(unittest.makeSuite(Get_InterfaceTest))

    result = BeautifulReport(test_suite)
    result.report(description='测试情况', filename='牛人榜测试报告',
                  log_path='./resource/report/')
