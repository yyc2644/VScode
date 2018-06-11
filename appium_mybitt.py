#encoding = utf-8
#基于appium的钱包自动化demo
import yaml
eth = yaml.load(open('E:/VScode_word/yaml/ETH_Private Key.yaml','r', encoding='UTF-8'))
eth = list(set(eth))

from appium_start import start_appium
from mybitt_testcase import ADD_Contact




# start_appium()

# 批量添加的时候这里加个参数
# print(eth)

for i  in eth:   
    ADD_Contact(i)
