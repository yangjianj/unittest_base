import HtmlTestRunner
import unittest
import xmlrunner

if __name__ == '__main__':
    test_suite = unittest.TestSuite()  # 创建一个测试集合
    all_cases = unittest.defaultTestLoader.discover('.','../test_case/task_*.py')
    # test_suite.addTest(unittest.makeSuite(MyTest))#使用makeSuite方法添加所有的测试方法
    fp = open('res.html', 'wb')  # 打开一个保存结果的html文件

    # 生成执行用例的对象
    for case in all_cases:
        #test_suite.addTests(case)
        test_suite.addTests(case)
        # runner = HtmlTestRunner.HTMLTestRunner(stream=fp, title='api测试报告', description='测试情况')
        # runner.run(test_suite)
        runner=xmlrunner.XMLTestRunner(output='report')
        runner.run(test_suite)
    # 执行测试套件