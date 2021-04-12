#!/usr/bin/env python
# -*- coding: utf-8 -*-
"""
@author:     leon
@contact:    576808577@qq.com
@others:     All by leon, All rights reserved-- Created on 2018/8/12
@desc:
"""
import unittest

from testProject.model.BigLan import testBigLanTest
from testProject.outputUtils.baselog import get_logger

log = get_logger()

class caselist(unittest.TestCase):

    log.info("开始运行所有的测试用例")


if __name__ == '__main__':

    unittest.main()

    testunit = unittest.TestSuite()

    testunit.addTest(testBigLanTest.test01_OP_Login("15021567126","admin"))
    testunit.addTest(testBigLanTest.test02_CreateDevice())
    testunit.addTest(testBigLanTest.test3_MerchantLogin())
    testunit.addTest(testBigLanTest.test04_MerchantCheckDevice())
    testunit.addTest(testBigLanTest.test04_MerchantCheckDevice())
    testunit.addTest(testBigLanTest.test04_MerchantCheckDevice())
    testunit.addTest(testBigLanTest.test04_MerchantCheckDevice())
    testunit.addTest(testBigLanTest.test04_MerchantCheckDevice())
    testunit.addTest(testBigLanTest.test04_MerchantCheckDevice())


    runner = unittest.TextTestRunner
    runner.run(testunit)

