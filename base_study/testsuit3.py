import sys
import unittest
class UserCase(unittest.TestCase):

    def testAddUser(self):
        print("add a user")

    def testDelUser(self):
        print("delete a user")

if __name__ == '__main__':
    module = __import__(__name__)
    suite = unittest.makeSuite(UserCase,prefix='test')
    suite2 = unittest.findTestCases(module,prefix='test')

    result = unittest.TextTestResult(sys.stdout, 'test result', 1)
    suite.run(result)