# -*- coding:utf-8 -*-
from selenium import webdriver
driver=webdriver.Chrome()
driver.get("https://www.bom2buy.com")
driver.find_element_by_link_text('登录').click()
driver.find_element_by_id('email-mobile').send_keys("jiahui@eefocus.com")
driver.find_element_by_id('password').send_keys("zjh112233")
driver.find_element_by_class_name('signin').click()
driver.find_element_by_link_text("退出").click()





