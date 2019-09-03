import sys
import unittest
class UserCase(unittest.TestCase):

    def testAddUser(self):
        print("add a user")

    def testDelUser(self):
        print("delete a user")

if __name__ == '__main__':
    #unittest.main()  #main方法入口
    result = unittest.TextTestResult(sys.stdout, 'test result', 1)
    case_obj = UserCase('testAddUser')
    case_obj.run(result)

