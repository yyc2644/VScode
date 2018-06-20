#encoding:UTF-8
#准备重构
#导入appium
from appium import webdriver
from time import sleep
import unittest
import yaml

eth_add = yaml.load(open('/Users/YiCheng/VSCode/yaml/eth_add.yaml','r',encoding = 'UTF-8'))

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
        self.d.implicitly_wait(10)


<<<<<<< HEAD
    # def test_FirstStard(self):
    #     self    
=======
    def test_FirstStard(self):
        pass    
>>>>>>> 59f656db650843f34c06501412b9f421d4e4b37f

    def test_Add_Trader(self):#添加联系人
        self.d.refresh
        #找到管理按钮并点击
        self.d.find_element_by_id("com.machain.mybitt:id/ivTabManage").click()
        #点击交易人 
        self.d.find_element_by_id("com.machain.mybitt:id/trContacts").click()
        j = 0
        for i in eth_add: 

            j = j+1
            eth = (str("eth")+str(j))
            self.d.refresh
            #点击添加
            self.d.find_element_by_id("com.machain.mybitt:id/menuAdd").click()
            #点击输入姓名
            self.d.find_element_by_id("com.machain.mybitt:id/etBackup").send_keys(eth)
            #点击选择币种
            self.d.find_element_by_id("com.machain.mybitt:id/trChoose").click()
            #选择eth
            self.d.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.TableRow[2]").click()
            #输入eth地址
            self.d.find_element_by_id("com.machain.mybitt:id/etAddress").send_keys(i)
            #保存联系人
            self.d.find_element_by_id("com.machain.mybitt:id/menuSave").click()
            print("完成保存",j,i)

    def test_Add_ETHWallet(self):
        self.d.refresh
        #找到管理按钮并点击
        self.d.find_element_by_id("com.machain.mybitt:id/ivTabManage").click()
        #点击管理钱包
        self.d.find_element_by_id("com.machain.mybitt:id/trManageWallet").click()
        #点击+号
        self.d.find_element_by_id("com.machain.mybitt:id/menuAdd").click()
        #点击导入钱包
        self.d.find_element_by_id("com.machain.mybitt:id/tvImportWallet").click()
        #点击跳过
        self.d.find_element_by_id("com.machain.mybitt:id/menuSkip").click()
        #选择eth钱包
        self.d.refresh
        self.d.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.LinearLayout/android.support.v7.widget.RecyclerView/android.widget.RelativeLayout[2]/android.widget.ImageView").click()
        #点击完成
        self.d.find_element_by_id("com.machain.mybitt:id/menuComplete").click()
        #选择私钥
        self.d.find_element_by_xpath("/hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout[1]/android.widget.LinearLayout/android.widget.RelativeLayout[2]").click()
        #输入私钥
        self.d.find_element_by_id("com.machain.mybitt:id/etKey").send_keys()
        #点击开始导入
        self.d.find_element_by_id("com.machain.mybitt:id/btnImport").click()
        #输入钱包名和两次密码
        self.d.find_element_by_id("com.machain.mybitt:id/etName").send_keys()
        self.d.find_element_by_id("com.machain.mybitt:id/etPwd").send_keys("qwe123")
        self.d.find_element_by_id("com.machain.mybitt:id/etPwdSure").send_keys("qwe123")

        #勾选服务协议
        self.d.find_element_by_id("com.machain.mybitt:id/cbAgreement").click()
        #点击完成导入
        self.d.find_element_by_id("com.machain.mybitt:id/btnCreateWallet").click()
        #点击开始使用
        self.d.find_element_by_id("com.machain.mybitt:id/btnStartUse").click()


    def tearDwon(self):
        try:
            self.d.quit()
        except:
            pass

if __name__ == '__main__':
    try:
        suite = unittest.TestLoader().loadTestsFromTestCase(DemoTest)
        unittest.TextTestRunner(verbosity=2).run(suite)
    except:
        pass
