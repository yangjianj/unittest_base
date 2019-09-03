# unittest_base
##unittest基础使用方法
###1.基本概念：test case,test suite,testLoader，test runner,test fixture。   
![概念图](images/unittest.JPG)    
test case：     
1.一个完整的测试单元，执行该测试单元可以完成对某一个问题的验证，完整体现在：测试前环境准备(setUp)，执行测试代码(run)，及测试后环境还原(tearDown)；     
2.测试方法的名称要以test开头。且只会执行以test开头定义的方法（测试用例）。     
test suite：    
1.多个测试用例的集合，测试套件或测试计划       
2.继承自unittest.TestCase      
testLoader  ：加载TestCase到TestSuite中的，其中loadTestsFrom__()方法用于寻找TestCase，并创建它们的实例，然后添加到TestSuite中，返回TestSuite实例；    
test runner ：执行测试用例，并将测试结果保存到TextTestResult实例中，包括运行了多少测试用例， 成功了多少，失败了多少等信息；    
test fixture：一个测试用例的初始化准备及环境还原，主要是setUp() 和 setDown()方法；    
2.测试Log生成：unittest_output_beautifulreport_ex1.py，unittest_output_HtmlTestRunner.py，unittest_output_txt.py    
3.测试结果信息收集：unittest_result_message_base.py，unittest_result_message_bf.py    
4.跳过用例：unittest_skip_case.py  
5.统计失败用例名，并将失败用例重跑方法？（精确筛选执行用例）  unittest_discover_base.py  
