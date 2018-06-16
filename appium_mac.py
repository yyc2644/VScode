#encoding:UTF-8
#准备重构
#导入appium
from appium import webdriver
from time import sleep
import unittest

eth_add = ["0xD91e4308eD4AB2aEb6eE532820bdb10cf7E914f3",
"0xdB46A59a11CFcBdAB9612559cf193A6Ac8aDC167",
"0xb7cadD7A4c3CAE480DA1bd7Df9510CE14B703066",
"0xeb8647572191B224E9C7437b1841C8441026c0E7",
"0xD185dc6C46A0bca21613Ec8a3b52c76732828Ca2",
"0x47f7AFdE2885Ec8a7334bD75Aff4E714A7B37820",
"0x5569241622B727c1025FFa276B87A4189bD2346F",
"0x3e7661fA8578476F05c16A3516a626CdC32B2B39",
"0xDE5C25E1F82B471c20D911704CaCF447735DeDE1",
"0x4aA9829a5282bCc9d2081Ee9eF23B855bfF1d066",
"0xdFceb91E927dF4884A1A76D7c6490c001D4def99",
"0x9ACEfCBbc06583D6f6DA1F10158A4231DcAC387d",
"0xF98111735a998169E392C9c746276832fBe03F1D",
"0x5803Cf668C8184413B6B5Ccae03b4B6d949685C1",
"0xd5f8fa3D43F03A974488CB33F533d35e0Ba71B0f",
"0xec518bCE5682B5cEF44E03d00EAdcc0c5a7e1514",
"0x9753d25c8f5EaA7d9A529D7D75c5f0E413870eD6",
"0xde1be0E76cd7D35597Ce806410f9Cd84656671b2",
"0x53d3a5a0544D2dC02B3f56D1E5cB0a90f167eab8",
"0xAdd2cBDaAe9EFD879E57a1bbAFA94AC2DD7Be776",
"0x70EAd276f145FbD4E8b2224E897fd32Bef1f3034",
"0x2286E9F079C6f9136f3CBf382bD2D9D8f552839e",
"0x0981240c43cEC260Cc1a81Aa5B0db51f3A9a069f",
"0x53d2EE617cBF7bb75F183391B16057923B3dC98A",
"0x16ABb8aA5De15ef3779c0B46574ff5516d58a5Bb",
"0xE01Aa85990Daa6c87D7B9c51091fB3b66411fb91",
"0xBd4E8d1E76Ba492479843A64d26799B70DbC74Ff",
"0x7F2Cc14791868CDdA463C4C29B0287e98ccD81BC",
"0xe055363f8088b507C452246A9516E7C7660C0e50",
"0x7F9c95bF0Ada6869b42b5c5930B0ff59F8bC251C",
"0xd476a5d17DA0C452738c45Aa4333C121b3A43D48",
"0x5dFada42F8a3b5FE7626Fc52E0989a43Cc1455B5",
"0xFf221f6f900e5449E7d69624bB0DBe7eFAdA66dd",
"0x2631156C9227fef988a14a49138371cb50d48D61",
"0x3aA481Df62B9Cf9e11fFABae0a9d899C59f1F3bD",
"0x83B21fd5Ae2e9EE40736FadCEb7be2898362961F",
"0xADEd986E42987a163b27964226fC8FC6dfDFc60C",
"0x986ECca3b71cD90e577cA814eB0812a3288b5f3c",
"0xf1B7edD07DE5DA01d86843b0a2d12dDcbbf2Fe28",
"0x1e4887EADe4cA31E04a60D02AddE5a48663d5d89",
"0x4EC8133aef2b9aBA90A8ad1722d5dFb8399F62Dd",
"0xD3B690b969cEb1AEDcD334c981B5F3C1B624D255",
"0x2B3108a3766A27eACDdB73F918E3BD7ce240F42F",
"0x65B1bc4C758C0852577296091aF14fa9Db74fb83",
"0x7D76569F6914F4c99AA9C27CfE681CE67aA27D1D",
"0x3b46E0a9A297ECfE0Caf14fb4807449CD88Ac787",
"0x5A8b60066d7E1943595b9e04E719Ac05a507D190",
"0xCebBe5b8285e658Fc3e4fEaf94348CB1eBd6C3a2",
"0xfFfcf51E1d9ec149E604A39C23CbaAF9e7d54f19",
"0xC892f74C059508D709e07E28af62F0a5816a7B4C",
"0xf8071130387c510871C8EfAb5b4f8Df14950183e",
"0xFd2e0be16cca810067580178e3B0C04528Db2dEB",
"0x48b4607Fde88288Cb0d604867Db16E2EF24b0Da5",
"0xc69A0E8f97f8AE5057db9968cc89646CDbC49c2a",
"0xb54E00475324ab7174c2F4A81E19D31c1272b11a",
"0x3Af31C69aFC46066D0C7dc8E898C1153E9C2242D"]

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


    def test_FirstStard(self):
        pass    

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
        print("完成保存",i)

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
