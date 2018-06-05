#encoding:UTF-8
#准备重构
#导入appium
from appium import webdriver
#
import os
import time

# appLocation ="C:\Users\Administrator\Desktop\app-release06_04_01.apk"
# aaptpath ="C:\Users\Administrator\AppData\Local\Android\Sdk\build-tools\27.0.3\aapt.exe"

# print (list(os.popen('adb devices').readlines()))

def get_os(x):
    return (os.popen(x)).readlines()

deviceName = 'adb devices'

print (list(get_os(deviceName)))
    


