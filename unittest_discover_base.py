#-*- coding:utf-8 -*-
import os
import unittest
from BeautifulReport import BeautifulReport
#执行测试用例的目录
case_path = os.path.join(os.getcwd(), 'test_case')  #这里填写你刚刚创建的case文件夹的目录
testsuit1 = unittest.TestSuite()
discover = unittest.defaultTestLoader.discover(case_path,pattern='test*.py',top_level_dir=None)
#discover方法筛选出来的用例，循环添加到测试套件中
'''  
print(discover)  #测试类集合  （unittest.suite.TestSuite）
print("11111111111111111111111")
for test_suits in discover:
    print(test_suits)   #单个测试类对象1 （unittest.suite.TestSuite）
    print("222222222222222222222222")
    for test_suit in test_suits:
        print(test_suit)   #单个测试类对象2 （unittest.suite.TestSuite）
        print("333333333333333333333333333333")
        for case in test_suit:
            print(case)    #测试实例（test2.MyTest2）=>文件名.类名
            print("4444444444444444444444444444444444")

'''

print(type(discover))
for test_suit_o in discover:
    for test_suit_i in test_suit_o:        #遍历测试类
        for test_case in test_suit_i:      #遍历测试类
            print("case message:",test_case)   #可进行精确筛选case
            testsuit1.addTest(test_case)  #逐个test_case进行添加，也可添加测试类test_suit_i
print(testsuit1)
result1=unittest.TestResult(stream=None, descriptions=None, verbosity=None)
#testsuit1.run(result1)
print("test result:",result1)

bf=BeautifulReport(testsuit1)
bf.report(filename='beautiful_report.html', description='搜索测试', log_path='report')