#启动appium
from appium import webdriver
import yaml


#设备基础信息全部写到GalaxyS8.yaml中
desired_caps = yaml.load(open("E:/VScode_word/yaml/GalaxyS8.yaml"))
#获取点击按钮的文本
element = yaml.load(open('E:/VScode_word/yaml/element.yaml','r', encoding='UTF-8'))
def start_appium():
    #设备基础信息全部写到GalaxyS8.yaml中
    desired_caps = yaml.load(open("E:/VScode_word/yaml/GalaxyS8.yaml"))
    #获取点击按钮的文本
    element = yaml.load(open('E:/VScode_word/yaml/element.yaml','r', encoding='UTF-8'))
    #启动driver
    driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

start_appium()