#encoding = utf-8
#基于appium的钱包自动化demo

from appium_start import start_appium
from mybitt_testcase import ADD_Contact


start_appium()

ADD_Contact()
