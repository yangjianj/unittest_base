import os
import unittest
from BeautifulReport import BeautifulReport

# 测试结果信息收集：
# 数据统计：总执行数，通过数，失败数，跳过数
# 时间统计：总开始时间，总运行时间，用例开始时间，用例运行时间（基本选项中没有时间统计信息需使用自己封装库例如:beautifulreport）
# case执行信息统计:case打印信息
# 失败信息统计：失败原因，失败case名,case所属类

if __name__ == '__main__':
    case_path = os.path.join(os.getcwd(), 'test_case')
    discover = unittest.defaultTestLoader.discover(case_path, pattern="test*.py", top_level_dir=None)
    bf=BeautifulReport(discover)
    bf.report(filename='beautiful_report.html', description='搜索测试', log_path='report')
    print("message")
    print(bf.FIELDS) #FIELDS属性存放所有执行结果
    print(bf.FIELDS['testAll'])
    print(bf.FIELDS['testPass'])
    print(bf.FIELDS['testFail'])
    print(bf.FIELDS['beginTime'])
    print(bf.FIELDS['totalTime'])
    print(bf.FIELDS['testSkip'])
    print(bf.FIELDS['testError'])
    for i in bf.FIELDS['testResult']:
        print(i['className'])
        print(i['methodName'])
        print(i['description'])
        print(i['spendTime'])
        print(i['status'])
        print(i['log'])
