import sys
import unittest
class UserCase(unittest.TestCase):

    def testAddUser(self):
        print("add a user")

    def testDelUser(self):
        print("delete a user")

if __name__ == '__main__':
    #多个case或多个suite可以构成一个suite
    suite = unittest.TestSuite(map(UserCase,['testAddUser','testDelUser']))
    suite2 = unittest.TestSuite()
    suite2.addTests(map(UserCase,['testAddUser','testDelUser']))
    suite3 = unittest.TestSuite()
    suite3.addTest(UserCase('testAddUser'))
    suite3.addTest(UserCase('testDelUser'))

    result = unittest.TextTestResult(sys.stdout, 'test result', 1)
    suite.run(result)