#encoding utf-8
from selenium import webdriver

# chromdriver_win = "C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe"
chromdriver_macos ="/Applications/chromedriver" 

# driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver = webdriver.Chrome(chromdriver_macos)
driver.get("http://www.baidu.com")