#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     leon
@contact:    576808577@qq.com
@others:     All by leon, All rights reserved-- Created on 2021/4/16
@desc:
"""
import time
import datetime
import json
import unittest

from testProject.config.configs import BaseUrl
from testProject.outputUtils import HTMLTestRunner
from testProject.outputUtils.casesSum import casesNumber
from testProject.testMethod import TestMethod
from testProject.outputUtils.baselog import get_logger
from testProject.utils.excelwrite import writeExcel
from testProject.outputUtils.output import new_report
from testProject.utils.responseInfo import regSearchString, assertResponse
from testProject.outputUtils.sendEmails import sendEmailFile

log = get_logger()

global caseName
global myWriteExcel
global base_url_op
global base_url_con
global access_token
global devicebatchNo
global merchantAccessToken
global failTimes


def test01_OP_Login(self, loginName="15021567126",password="admin"):
    log.info("----------1登录OP运营平台--------开始测试")
    global base_url_op
    global base_url_con
    global myWriteExcel
    myWriteExcel = writeExcel(new_report('APIcaseReport'))
    caseID = 1
    global caseName
    caseName = "1登录OP运营平台"
    global access_token
    global failTimes
    failTimes = 0
    method = "post"
    headers = {'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, br',
               'Content-Type': 'application/json; charset=utf-8'}
    baseUrl = base_url_op
    parameters = "/api/v2/op/pub/login"
    bodyData = {"loginName": loginName, "password": password, "loginType": "PASSWORD", "type": "account"}
    asserts = "商家中心"
    log.info("先将前几个前提信息写入Excel表中")
    myWriteExcel.writePreconditions(caseID + 1, caseID, caseName, method, str(headers), baseUrl,
                                    parameters, str(bodyData), asserts)

    url = baseUrl + parameters
    log.info("调用getMethod方法")
    response = TestMethod.postMethod(self, url, bodyData, headers)

    try:
        if "200" in str(response):
            myWriteExcel.writeStatusCode(caseID + 1, "200 OK")
            myWriteExcel.writeResponse(caseID + 1, response.text)
            myWriteExcel.saveExcel()
            log.info(caseName + " 测试结果StatusCode----200 OK----- " + str(response))

            if assertResponse(asserts, response.text):
                # 这里没有考虑到需要断言多个信息
                myWriteExcel.writeAssertResult(caseID + 1, "Pass")
                myWriteExcel.writeResult(caseID + 1, "Pass")
                myWriteExcel.writeErrorReason(caseID + 1, "NO")
                # "accessToken":"2cd1bbce-362a-4f4e-b779-8f56702d0a96"},
                access_token = regSearchString(response.text, '"accessToken":"(.+?)"},', 15, -3)
                print(access_token)

            else:
                myWriteExcel.writeAssertFailResult(caseID + 1, "Fail")
                myWriteExcel.writeFailResult(caseID + 1, "Fail")
                myWriteExcel.writeErrorReason(caseID + 1, "断言失败")
                failTimes = failTimes + 1

        else:
            myWriteExcel.writeStatusCode(caseID + 1, response)
            myWriteExcel.writeResponse(caseID + 1, response)
            myWriteExcel.writeAssertFailResult(caseID + 1, "Fail")
            myWriteExcel.writeFailResult(caseID + 1, "Fail")
            myWriteExcel.writeErrorReason(caseID + 1, response)
            log.info(caseName + " 测试结果StatusCode 不是 200 OK----- " + response)
            failTimes = failTimes + 1

    except Exception as e:
        log.info("将测试失败（运行代码失败，接口发送请求失败）的错误原因写入Excel的“备注” 里面")
        myWriteExcel.writeRemarks(caseID + 1, e)
        log.info(e)
    myWriteExcel.writeDurationTime(caseID + 1, response.elapsed.microseconds)
    log.info("最后保存excel")
    myWriteExcel.saveExcel()
    log.info("----------1登录OP运营平台--------测试完毕")





def test02_CreateDevice(self,deviceCode="device11111111",hardwareCode="code1111111"):
    log.info("----------2创建大兰设备--------开始测试")
    global devicebatchNo
    global access_token
    global myWriteExcel
    myWriteExcel = writeExcel(new_report('APIcaseReport'))
    caseID = 2
    global caseName
    caseName = "2创建大兰设备"
    global failTimes
    method = "post"
    headers = {'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, br',
               'Content-Type': 'application/json; charset=utf-8', 'Authorization': 'Bearer  ' + access_token}
    print("headers--------------------" + str(headers))
    baseUrl = "https://test-op.quixmart.com"
    parameters = "/api/v2/op/device"
    # 以13位的时间戳作为deviceCode
    # nowTime = lambda: int(round(time.time() * 1000))
    # deviceCode = str(nowTime())
    # print("deviceCode--------" + deviceCode)
    # hardwareCode = '2018' + deviceCode
    bodyData = {"productCode": "BIGLAN", "versionCode": "DBV1300", "editionCode": "V1",
                "list": [{"hardwareCode": hardwareCode, "producedTime": "2018-08-01", "deviceCode": deviceCode}]}
    asserts = "请求成功"
    log.info("先将前几个前提信息写入Excel表中")
    myWriteExcel.writePreconditions(caseID + 1, caseID, caseName, method, str(headers), baseUrl,
                                    parameters, str(bodyData), asserts)
    url = baseUrl + parameters
    log.info("调用getMethod方法")
    response = TestMethod.postMethod(self, url, bodyData, headers)

    try:
        if "200" in str(response):
            myWriteExcel.writeStatusCode(caseID + 1, "200 OK")
            myWriteExcel.writeResponse(caseID + 1, response.text)
            myWriteExcel.saveExcel()
            log.info(caseName + " 测试结果StatusCode----200 OK----- " + str(response))

            if assertResponse(asserts, response.text):
                # 这里没有考虑到需要断言多个信息
                myWriteExcel.writeAssertResult(caseID + 1, "Pass")
                myWriteExcel.writeResult(caseID + 1, "Pass")
                myWriteExcel.writeErrorReason(caseID + 1, "NO")
                # 获取设备批次号devicebatchNo   "data":349,
                devicebatchNo = regSearchString(response.text, '"data":(.+?),', 7, -1)

            else:
                myWriteExcel.writeAssertFailResult(caseID + 1, "Fail")
                myWriteExcel.writeFailResult(caseID + 1, "Fail")
                myWriteExcel.writeErrorReason(caseID + 1, "断言失败")
                failTimes = failTimes + 1

        else:
            myWriteExcel.writeStatusCode(caseID + 1, response)
            myWriteExcel.writeResponse(caseID + 1, response)
            myWriteExcel.writeAssertFailResult(caseID + 1, "Fail")
            myWriteExcel.writeFailResult(caseID + 1, "Fail")
            myWriteExcel.writeErrorReason(caseID + 1, response)
            log.info(caseName + " 测试结果StatusCode 不是 200 OK----- " + response)
            failTimes = failTimes + 1

    except Exception as e:
        log.info("将测试失败（运行代码失败，接口发送请求失败）的错误原因写入Excel的“备注” 里面")
        myWriteExcel.writeRemarks(caseID + 1, e)
        log.info(e)
    myWriteExcel.writeDurationTime(caseID + 1, response.elapsed.microseconds)
    log.info("最后保存excel")
    myWriteExcel.saveExcel()
    log.info("----------2创建设备--------测试完毕")






def test3_MerchantLogin(self,loginName="15689526503",password="123456"):
    log.info("----------3登录商家平台--------开始测试")
    global merchantAccessToken
    global myWriteExcel
    myWriteExcel = writeExcel(new_report('APIcaseReport'))
    caseID = 3
    global caseName
    caseName = "3登录商家平台"
    global failTimes
    method = "post"
    headers = {'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, br',
               'Content-Type': 'application/json; charset=utf-8'}
    print("headers--------------------" + str(headers))
    baseUrl = "https://test-console.quixmart.com"
    parameters = "/api/v2/merchant/pub/login"
    print("parameters--------------------" + parameters)

    bodyData = {"loginName": loginName, "password": password, "loginType": "PASSWORD", "type": "account"}
    asserts = "jz66666"
    print(asserts)
    log.info("先将前几个前提信息写入Excel表中")
    myWriteExcel.writePreconditions(caseID + 1, caseID, caseName, method, str(headers), baseUrl,
                                    parameters, str(bodyData), asserts)

    url = baseUrl + parameters
    log.info("调用postMethod方法")
    response = TestMethod.postMethod(self, url, bodyData, headers)

    try:
        if "200" in str(response):
            myWriteExcel.writeStatusCode(caseID + 1, "200 OK")
            myWriteExcel.writeResponse(caseID + 1, response.text)
            myWriteExcel.saveExcel()
            log.info(caseName + " 测试结果StatusCode----200 OK----- " + str(response))

            if assertResponse(asserts, response.text):
                # 这里没有考虑到需要断言多个信息
                myWriteExcel.writeAssertResult(caseID + 1, "Pass")
                myWriteExcel.writeResult(caseID + 1, "Pass")
                myWriteExcel.writeErrorReason(caseID + 1, "NO")
                # 获取商家平台accessToken   "id":1341,
                merchantAccessToken = regSearchString(response.text, '"accessToken":"(.+?)"', 15, -1)
                print(merchantAccessToken)

            else:
                myWriteExcel.writeAssertFailResult(caseID + 1, "Fail")
                myWriteExcel.writeFailResult(caseID + 1, "Fail")
                myWriteExcel.writeErrorReason(caseID + 1, "断言失败")
                failTimes = failTimes + 1

        else:
            myWriteExcel.writeStatusCode(caseID + 1, response)
            myWriteExcel.writeResponse(caseID + 1, response)
            myWriteExcel.writeAssertFailResult(caseID + 1, "Fail")
            myWriteExcel.writeFailResult(caseID + 1, "Fail")
            myWriteExcel.writeErrorReason(caseID + 1, response)
            log.info(caseName + " 测试结果StatusCode 不是 200 OK----- " + response)
            failTimes = failTimes + 1

    except Exception as e:
        log.info("将测试失败（运行代码失败，接口发送请求失败）的错误原因写入Excel的“备注” 里面")
        myWriteExcel.writeRemarks(caseID + 1, e)
        log.info(e)
    myWriteExcel.writeDurationTime(caseID + 1, response.elapsed.microseconds)
    log.info("最后保存excel")
    myWriteExcel.saveExcel()
    log.info("----------3登录商家平台--------测试完毕")




def test04_MerchantCheckDevice(self):
    log.info("----------4商家查询设备--------开始测试")
    global deviceCode
    global merchantAccessToken
    global myWriteExcel
    myWriteExcel = writeExcel(new_report('APIcaseReport'))
    caseID = 4
    global caseName
    caseName = "4商家查询设备"
    global failTimes
    method = "get"
    headers = {'Accept': 'application/json', 'Accept-Encoding': 'gzip, deflate, br',
               'Content-Type': 'application/json; charset=utf-8', 'Authorization': 'Bearer  ' + merchantAccessToken}
    print("headers--------------------" + str(headers))
    baseUrl = "https://test-console.quixmart.com"
    parameters = "/api/v2/merchant/devices/_search?pageNumber=1&pageSize=10&deviceCode={deviceCode}&status=ONLINE,SELLED,RENT,TROUBLE,MAINTAIN,UPDATING,REPLENISHING".format(
        deviceCode=int(deviceCode))
    print("parameters--------------------" + parameters)

    bodyData = ""
    asserts = "请求成功"
    print(asserts)
    log.info("先将前几个前提信息写入Excel表中")
    myWriteExcel.writePreconditions(caseID + 1, caseID, caseName, method, str(headers), baseUrl,
                                    parameters, str(bodyData), asserts)

    url = baseUrl + parameters
    log.info("调用getMethod方法")
    response = TestMethod.getMethod(self, url, headers)

    try:
        if "200" in str(response):
            myWriteExcel.writeStatusCode(caseID + 1, "200 OK")
            myWriteExcel.writeResponse(caseID + 1, response.text)
            myWriteExcel.saveExcel()
            log.info(caseName + " 测试结果StatusCode----200 OK----- " + str(response))

            if assertResponse(asserts, response.text):
                # 这里没有考虑到需要断言多个信息
                myWriteExcel.writeAssertResult(caseID + 1, "Pass")
                myWriteExcel.writeResult(caseID + 1, "Pass")
                myWriteExcel.writeErrorReason(caseID + 1, "NO")
                # 获取deviceSearchId   "id":1348,
                deviceSearchId = regSearchString(response.text, '"id":(.+?),', 5, -1)
                print("deviceSearchId-------" + deviceSearchId)

            else:
                myWriteExcel.writeAssertFailResult(caseID + 1, "Fail")
                myWriteExcel.writeFailResult(caseID + 1, "Fail")
                myWriteExcel.writeErrorReason(caseID + 1, "断言失败")
                failTimes = failTimes + 1

        else:
            myWriteExcel.writeStatusCode(caseID + 1, response)
            myWriteExcel.writeResponse(caseID + 1, response)
            myWriteExcel.writeAssertFailResult(caseID + 1, "Fail")
            myWriteExcel.writeFailResult(caseID + 1, "Fail")
            myWriteExcel.writeErrorReason(caseID + 1, response)
            log.info(caseName + " 测试结果StatusCode 不是 200 OK----- " + response)
            failTimes = failTimes + 1

    except Exception as e:
        log.info("将测试失败（运行代码失败，接口发送请求失败）的错误原因写入Excel的“备注” 里面")
        myWriteExcel.writeRemarks(caseID + 1, e)
        log.info(e)
    myWriteExcel.writeDurationTime(caseID + 1, response.elapsed.microseconds)
    log.info("最后保存excel")
    myWriteExcel.saveExcel()
    log.info("----------4商家查询设备--------测试完毕")