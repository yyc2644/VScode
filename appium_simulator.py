#encoding:UTF-8
#用appium链接模拟器进行调试

#这个文件废弃了，模拟器上面的appium坑有点多，目前卡在adb命令上面
#adb可以用模拟器自带的adb替换AS

from appium import webdriver
desired_caps = {}
#设置自动化参数
desired_caps['platformName'] = 'Android'
# adb devices
desired_caps['deviceName'] = '127.0.0.1:62001'

#设置安卓系统版本
# adb shell getprop ro.build.version.release
desired_caps['platformVersion'] = '4.4.2'
#设置apk路径


#设置app的主包名和主类名
#adb shell pm list package
#第二个命令，aapt的地址 + dump badging + app地址
#C:\Users\Administrator\AppData\Local\Android\Sdk\build-tools\27.0.3\aapt.exe dump badging C:\Users\Administrator\Desktop\Mybitt_test_api.apk
#launchable-activity: name='com.machain.module.main.ui.welcome.WelcomeActivity'

desired_caps['appPackage'] = 'com.machain.mybitt'
desired_caps['appActivity'] = 'com.machain.module.main.ui.welcome.WelcomeActivity'

#设置输入的编码
desired_caps['unicodeKeyboard'] = 'True'
desired_caps['resetKeyboard'] = 'True'

#初始化
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)