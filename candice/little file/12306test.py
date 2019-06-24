from selenium import webdriver
# from selenium.webdriver.common.keys import Keys
driver =webdriver.Chrome()
driver.set_window_size(1080,800)
driver.implicitly_wait(10)
driver.get('https://www.12306.cn/index/index.html')
driver.find_element_by_class_name('service-icon ico-s2').click()


