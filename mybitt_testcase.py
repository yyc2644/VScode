from appium import webdriver
from time import sleep
import unittest
import yaml



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
driver = webdriver.Remote(remote, desired_caps)
driver.implicitly_wait(10)

driver.refresh
#找到管理按钮并点击
driver.find_element_by_id("com.machain.mybitt:id/ivTabManage").click()
#点击管理钱包
driver.find_element_by_id("com.machain.mybitt:id/trManageWallet").click()
#点击+号
driver.find_element_by_id("com.machain.mybitt:id/menuAdd").click()
#点击导入钱包
driver.find_element_by_id("com.machain.mybitt:id/tvImportWallet").click()
#点击跳过
driver.find_element_by_id("com.machain.mybitt:id/menuSkip").click()
#选择eth钱包
driver.refresh
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.ImageView").click()
#点击完成
driver.find_element_by_id("com.machain.mybitt:id/menuComplete").click()
#选择私钥
driver.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout[2]").click()
#输入私钥
driver.find_element_by_id("com.machain.mybitt:id/etKey").send_keys("32d5f62d24e6309afa3eed924fb2409a9dd1b1ed86e1ff4abd4bd159b7b63df0")
#点击开始导入
driver.find_element_by_id("com.machain.mybitt:id/btnImport").click()
#输入钱包名和两次密码
driver.find_element_by_id("com.machain.mybitt:id/etName").send_keys("eth1")
driver.find_element_by_id("com.machain.mybitt:id/etPwd").send_keys("qwe123")
driver.find_element_by_id("com.machain.mybitt:id/etPwdSure").send_keys("qwe123")

#勾选服务协议
driver.find_element_by_id("com.machain.mybitt:id/cbAgreement").click()
#点击完成导入
driver.find_element_by_id("com.machain.mybitt:id/btnCreateWallet").click()
#点击开始使用
driver.find_element_by_id("com.machain.mybitt:id/btnStartUse").click()

print("添加成功")