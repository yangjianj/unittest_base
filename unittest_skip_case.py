import HtmlTestRunner
import time
import unittest
from myfunction import *
from config import environment

@unittest.skip("showing class skipping")  #整个类跳过
class MyTest_skip(unittest.TestCase):  # 继承unittest.TestCase
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

    @unittest.skip('no reason skipping')   #无条件跳过
    def test_run(self):
        # self.assertEqual(1,1)
        self.assertIs(1, 2)
        print(time.localtime())
        time.sleep(3)
        self.assertEqual(3,add(1,2))  #对待测方法进行测试
        # 测试用例

    @unittest.skipIf(environment.VERSION>1,'version not supported')  #满足条件跳过
    def test_run2(self):
        # self.assertEqual(1,1)
        self.assertIs(1, 1)
        print(time.localtime())
        time.sleep(2)
        self.assertEqual(-1, mins(1, 2))  # 对待测方法进行测试
        # 测试用例

    @unittest.skipUnless(environment.VERSION>1,'version not supported') #不满足条件跳过
    def test_run3(self):
        # self.assertEqual(1,1)
        time.sleep(10)
        print(time.localtime())
        self.assertIs(1, 1)
        # 测试用例

    def test_run1(self):
        # self.assertEqual(1,1)
        print(time.localtime())
        time.sleep(3)
        self.assertIs(1, 1)
        # 测试用例
if __name__ == '__main__':
    unittest.main()  #执行case