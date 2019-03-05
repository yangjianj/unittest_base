import os
import unittest
#测试结果信息收集：
if __name__ == '__main__':
    case_path = os.path.join(os.getcwd(), 'test_case')
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)
    test_result = unittest.TextTestRunner(verbosity=2).run(discover)
    print('All case number')
    print(test_result.testsRun)
    print('Failed case number')
    print(len(test_result.failures))
    print('Failed case and reason')
    print(test_result.failures)
    for case, reason in test_result.failures:
        print(case.id())
        print(reason)

    print('skiped case')
    print(test_result.skipped)
    print('expectedFailures case')
    print(test_result.expectedFailures)
    print('unexpectedSuccesses case')
    print(test_result.unexpectedSuccesses)
    print('errors case')
    print(test_result.errors)