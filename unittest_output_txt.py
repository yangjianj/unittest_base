import os
import unittest
#测试结果信息收集：
if __name__ == '__main__':
    case_path = os.path.join(os.getcwd(), 'test_case')
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)
    reportpath = os.path.join(os.getcwd(), 'report','test_report.txt')
    with open(reportpath,'a') as f:
        runner = unittest.TextTestRunner(stream=f,verbosity=2)
        runner.run(discover)