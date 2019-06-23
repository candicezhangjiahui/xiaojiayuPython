# -*- coding:utf-8 -*-
from selenium import webdriver
browser = webdriver.Chrome()
browser.get('https://www.baidu.com')
print(browser.page_source) //browser.page_source是获取网页的全部html
browser.close()
print(browser.title)  # 获取网页的title
browser.quit()




