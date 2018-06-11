#encoding:UTF-8
#准备重构
#导入appium
from appium import webdriver
import PyYAML
import os
import time
import appium_util

#设备基础信息全部写到GalaxyS8.yaml中
desired_caps = yaml.load(open("E:/VScode_word/yaml/GalaxyS8.yaml"))

#获取点击按钮的文本
element = yaml.load(open('E:/VScode_word/yaml/element.yaml','r', encoding='UTF-8'))

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
    driver.refresh

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

def ADD_Contact():
    appium_util.wait_5()
    #找到管理按钮并点击
    appium_util.click_id(element['ivTabManage'])

    #点击交易人 
    appium_util.click_id(element['trContacts'])

    #点击添加
    appium_util.click_id(element['menuAdd'])

    #点击输入姓名
    appium_util.send_id(element['name'],"ethb")
    
    #点击选择币种
    appium_util.click_id(element['trChoose'])

    #选择eth
    appium_util.wait_5()
    appium_util.click_xpath(element['ChooseETH'])

    #输入eth地址
    appium_util.wait_5()
    appium_util.send_id(element['etAddress'],element['ethlocal2'])

    #保存联系人
    appium_util.click_id(element['menuSave'])

    print("完成保存联系人")
    

ADD_Contact()
    


