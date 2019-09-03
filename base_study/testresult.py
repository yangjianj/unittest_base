#unittest_prac.py
import unittest
import sys
#扩展TestResult
class MyTestResult(unittest.TestResult):

    def startTest(self, test):
        #此方法是在用例准备执行之前会被调用一次
        print('startTest')

    def startTestRun(self):
        print('startTestRun')

    def stopTest(self, test):
        print('stopTest')

    def stopTestRun(self):
        #在所有用例执行完成之后被调用。跟startTestRun类似，当我们传入的参数result为None时，才会去执行这个方法
        print('stopTestRun')
    '''
	其他可扩展方法方法是针对测试用例执行的结果处理： 
	addFailure：测试用例error的时处理
	addSuccess：测试用例执行成功时处理
	addSkip：测试用例跳过时处理
	addExpectedFailure：测试用例执行跟预期结果不一样，不如assert断言
	addUnexpectedSuccess：测试用例结果期望失败，但最后成功了。
	'''

class UnitTestCase(unittest.TestCase):

    def setUp(self):
        print("setup")

    def test01(self):
        print('test01')

    def tearDown(self):
        print('teardown')

if __name__ == '__main__':
    result = MyTestResult(sys.stdout,'test result',1)
    testcase = UnitTestCase('test01')
    testcase.run(result) #注意此处我传入了result参数