#encoding:UTF-8
#准备重构
#导入appium
from appium import webdriver
from time import sleep
import unittest

class DemoTest(unittest.TestCase):
    def setUp(self):
        desired_caps={"platformName": "Android",
                        "deviceName": "988a1c394a41385544",
                        "platformVersion": "7.0",
                        "noReset": True,
                        "resetKeyboard": True,
                        "appPackage":"com.machain.mybitt",
                        "appActivity":"com.machain.module.main.ui.welcome.WelcomeActivity",
                        "unicodeKeyboard":True,
                        }
        remote = "http://127.0.0.1:4723/wd/hub"    
        self.d = webdriver.Remote(remote, desired_caps)

    def Add_Trader(self):
        sleep(3)
        self.d.refresh
        




