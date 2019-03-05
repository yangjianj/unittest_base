import HtmlTestRunner
import time
import unittest
import xmlrunner
from myfunction import *

class MyTest1(unittest.TestCase):  # 继承unittest.TestCase
    def tearDown(self):
        # 每个测试用例执行之后做操作
        print('in teardown')

    def setUp(self):
        # 每个测试用例执行之前做操作
        print('in setup')

    @classmethod
    def tearDownClass(cls): #每个测试套件执行之后动作
        print('in teardownclass')

    @classmethod
    def setUpClass(cls): #每个测试套件执行之前动作
        print('in setUpClass')

    def test_run(self):
        # self.assertEqual(1,1)
        self.assertIs(1, 1)
        print(time.localtime())
        time.sleep(3)
        result=self.assertEqual(3,add(1,2))  #对待测方法进行测试
        print('11111111111 in test ')
        print(result)
        # 测试用例

    def test_run2(self):
        # self.assertEqual(1,1)
        self.assertIs(1, 1)
        print(time.localtime())
        time.sleep(4)
        self.assertEqual(-1, mins(1, 2))  # 对待测方法进行测试
        # 测试用例

    def test_run3(self):
        # self.assertEqual(1,1)
        print("111111111111111111111")
        print(time.localtime())
        time.sleep(5)
        self.assertIs(1, 1)
        # 测试用例

    def test_run1(self):
        # self.assertEqual(1,1)
        self.assertIs(1, 1)
        print(time.localtime())
        time.sleep(6)
        # 测试用例
if __name__ == '__main__':
     test_suite = unittest.TestSuite()    #创建一个测试集合
     test_suite.addTest(MyTest1('test_run1'))#测试套件中添加测试用例
     #test_suite.addTest(unittest.makeSuite(MyTest))#使用makeSuite方法添加MyTest类中所有的测试方法。
     fp = open('res.html','wb')   #打开一个保存结果的html文件
     # runner = HtmlTestRunner.HTMLTestRunner(stream=fp,title='api测试报告',description='测试情况')  #生成执行用例的对象
     # runner.run(test_suite)    #执行测试套件
     # unittest.TextTestRunner().run(test_suite)
     runner=xmlrunner.XMLTestRunner(output='report')
     runner.run(test_suite)
     print('test end')
     print(unittest.TestResult)