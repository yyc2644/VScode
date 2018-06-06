#encoding = UTF-8
#尝试不安装直接启动手机里的app
from appium import webdriver
import time

#交易人id
trContacts = "com.machain.mybitt:id/trContacts"
#添加钱包按钮
menuAdd = "com.machain.mybitt:id/menuAdd"
#姓名
name = "com.machain.mybitt:id/etBackup"

#币种下拉框
trChoose = "com.machain.mybitt:id/trChoose"

#选择币种
ChooseETH = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.TableRow[2]"
ChooseBTC = "/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.TableRow[1]"
#输入币种地址
etAddress = "com.machain.mybitt:id/etAddress"
#eth测试地址
ethlocal1 = "0xf1ac2A5246fC2250e0eB47c1A59eEC93b3e41881"

ethlocal2 = "0xa875F6e358E33b5e29793b5DE9d139359e074D6d"

#资产按钮
llTabProperty = "com.machain.mybitt:id/llTabProperty"
#行情按钮
llTabMarket = "com.machain.mybitt:id/llTabMarket"
#资讯按钮
llTabInfo = "com.machain.mybitt:id/llTabInfo"
#管理按钮
llTabManage = "com.machain.mybitt:id/llTabManage"
ivTabManage= "com.machain.mybitt:id/ivTabManage"

#保存按钮
menuSave = "com.machain.mybitt:id/menuSave"

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = '988a1c394a41385544 '
desired_caps['platformVersion'] = '7.0'
desired_caps['noReset'] = 'true'
desired_caps['resetKeyboard'] = 'true'
desired_caps['appPackage'] = 'com.machain.mybitt'
desired_caps['appActivity'] = 'com.machain.module.main.ui.welcome.WelcomeActivity'
desired_caps['unicodeKeyboard'] = 'True'
desired_caps['resetKeyboard'] = 'True'

#初始化
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

#添加联系人
def ADD_Contact():
    time.sleep(5)
    driver.refresh
    print("等待并刷新")
    #找到管理按钮并点击
    driver.find_element_by_id(ivTabManage).click()

    #点击交易人   
    driver.find_element_by_id(trContacts).click()

    #点击添加
    driver.find_element_by_id(menuAdd).click()

    #点击输入姓名
    driver.find_element_by_id(name).send_keys("ethb")
    
    #点击选择币种
    # time.sleep(5)
    driver.find_element_by_id(trChoose).click()

    #选择eth
    time.sleep(5)
    driver.refresh
    print("refresh and sleep and click")
    driver.find_element_by_xpath(ChooseETH).click()

    #输入eth地址
    time.sleep(5)
    driver.refresh
    driver.find_element_by_id(etAddress).send_keys(ethlocal2)

    #保存联系人
    driver.find_element_by_id(menuSave).click()

    print("完成保存联系人")
    


ADD_Contact()