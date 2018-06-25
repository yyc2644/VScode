from selenium import webdriver

driver = webdriver.Chrome("C:\Program Files (x86)\Google\Chrome\Application\chromedriver.exe")
driver.get("http://192.168.1.248:9079/#/home")
#点击注册
driver.find_element_by_xpath('//*[@id="app"]/div/div[1]/div/div/div[3]/div[1]/button[2]').click
driver.refresh
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[2]/div[3]/label[2]').click
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[2]/div[4]/form/div[1]/div/div/input').send_keys("qwe123@qwe.com")
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[2]/div[3]/label[2]').click
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[2]/div[4]/form/div[2]/div/div[1]/div/div[1]/div/input').send_keys("101010")
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[2]/div[4]/form/div[3]/div/div[1]/input').send_keys("qwe123")
driver.find_element_by_xpath('//*[@id="app"]/div/div[2]/div/div/div[2]/div/div/div[2]/div[4]/form/div[5]/div/button').click()