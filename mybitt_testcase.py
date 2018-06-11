import appium_util

import yaml

element = yaml.load(open('E:/VScode_word/yaml/element.yaml','r', encoding='UTF-8'))

#将测试用例整合到这里
def ADD_Contact(keys):

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
    appium_util.send_id(element['etAddress'],keys)

    #保存联系人
    appium_util.click_id(element['menuSave'])

    print("完成保存联系人")
    

# ADD_Contact()
    