#encoding:UTF-8
#准备重构
#导入appium
from appium import webdriver
import yaml
import os
import time

#设备基础信息全部写到GalaxyS8.yaml中
desired_caps = yaml.load(open("E:/VScode_word/yaml/GalaxyS8.yaml"))

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)






    


