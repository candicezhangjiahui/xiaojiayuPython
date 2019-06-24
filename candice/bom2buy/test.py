# -*- coding:utf-8 -*-
from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
driver =webdriver.Chrome()
driver.implicitly_wait(10)
driver.get('https://www.bom2buy.com')
driver.find_element_by_link_text('登录').click()
# driver.findElement(By.xpath("//a[@href='systemConfigAction.do?method=edit&id=40']"));



