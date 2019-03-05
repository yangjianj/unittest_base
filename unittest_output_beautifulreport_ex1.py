import os
import unittest
from BeautifulReport import BeautifulReport
 #结合BeautifulReport 生成报告

if __name__ == '__main__':
    case_path = os.path.join(os.getcwd(), 'test_case')
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)
    bf=BeautifulReport(discover)
    bf.report(filename='beautiful_report.html', description='搜索测试', log_path='report')