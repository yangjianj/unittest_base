import sys
import unittest
class UserCase(unittest.TestCase):

    def testAddUser(self):
        print("add a user")

    def testDelUser(self):
        print("delete a user")

if __name__ == '__main__':
    module = __import__(__name__)
    suite = unittest.TestLoader().discover('.','unittest_user.py') #unittest_user.py
    suite2 = unittest.TestLoader().loadTestsFromTestCase(UserCase)
    suite3 = unittest.TestLoader().loadTestsFromModule(module)
    #loadTestsFromName、loadTestsFromNames暂时不举例了，参数类型较多，不便举例，可以自行阅读其代码
    result = unittest.TextTestResult(sys.stdout, 'test result', 1)
    suite.run(result)