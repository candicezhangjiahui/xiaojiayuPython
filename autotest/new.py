#encoding = utf-8
from selenium import webdriver


from selenium import webdriver
import time
#通过executable_path参数指定Firefox驱动文件所在位置
driver = webdriver.Firefox(executable_path="D:\\geckodriver")
#打开百度首页
driver.get("http://www.baidu.com")
#获得输入框id
inputID = driver.find_elements_by_id("kw")
inputID.clear()
#在框内输入搜索内容
inputID.send_keys(u"自动化测试")
#单击搜索按钮
driver.find_elements_by_id("su").click()
#等待3秒
time.sleep(3)
#退出浏览器
