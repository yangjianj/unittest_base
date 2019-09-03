import unittest
import time
class DefaultTestCase(unittest.TestCase):

    def setUp(self):
        print("Start to run")

    def tearDown(self):
        print("Close")


class CasesALL(DefaultTestCase):

    def ab_test_print_b(self):
        print('b')
        print(time.time())
        time.sleep(2)