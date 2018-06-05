#encoding = utf-8
#基于appium的钱包自动化demo

import unittest
import appium

class TestStringMethods(unittest.TestCase):
    def setUp():
        print("start")
    def tearDown():
        print("stop")
    def test_open(self):
        print("run 1")
        

if __name__ == '__main__':
    unittest.main()