
from appium import webdriver

import time

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
#定义事件
def click_id(ele):
    driver.find_element_by_id(ele).click()
#找不到id的就用xpath
def click_xpath(ele):
    driver.find_element_by_xpath(ele).click()
def send_id(ele,keys):
    driver.find_element_by_id(ele).send_keys(keys)
#部分有页面跳转的情况，先等待，再刷新，再继续操作
def wait_5():
    time.sleep(5)
