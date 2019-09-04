import unittest
class UserCase(unittest.TestCase):

    def testAddUser(self):
        print("add a user")

    def testDelUser(self):
        print("delete a user")

if __name__ == '__main__':
    pass
    runner = unittest.TextTestRunner()
    #suite = unittest.TestSuite(map(UserCase,['testAddUser','testDelUser']))
    #case = UserCase('testAddUser')

    #runner.run(suite)
    #runner.run(case)