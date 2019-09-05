import unittest
from unittest import TestLoader
import for_loader
from for_loader import CasesALL
'''
loadTestsFromTestCase(testCaseClass) 
testCaseClass必须是TestCase的子类（或孙类也行）

loadTestsFromModule(module, pattern=None) 
test case所在的module

loadTestsFromName(name, module=None) 
name是一个string，string需要是是这种格式的“module.class.method”

loadTestsFromNames(name, module=None) 
names是一个list，用法与上同

discover(start_dir, pattern=’test*.py’, top_level_dir=None) 
从python文件中获取test cases
'''
if __name__ == '__main__':
    suite = unittest.TestSuite()
    loader = TestLoader()
    loader.testMethodPrefix = 'ab'
    # loader.sortTestMethodsUsing = None
    # test_cases_name = loader.getTestCaseNames(CasesALL)
    test_cases1 = unittest.TestLoader().loadTestsFromTestCase(CasesALL)
    test_cases2 = unittest.TestLoader().loadTestsFromModule(for_loader)
    test_cases3 = unittest.TestLoader().loadTestsFromName('for_loader.TestCase1.ab_test_print_b')

    #目录+文件名匹配：存放用例的目录属性必须是python package，必须要有__init__.py；否则不会遍历子目录
    discover = unittest.defaultTestLoader.discover(casedir, pattern="ui_lianjia*.py", top_level_dir=None) 
    suite.addTests(test_cases1)
    suite.addTests(test_cases2)
    suite.addTests(test_cases3)
    runner = unittest.TextTestRunner(verbosity=2)
    runner.run(suite)
