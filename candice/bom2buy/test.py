# -*- coding:utf-8 -*-
from selenium import webdriver
from selenium.webdriver.common.by import By
driver=webdriver.Chrome()
# driver.get("https://www.bom2buy.com")
# driver.find_element_by_link_text('登录').click()
# driver.find_element_by_id('email-mobile').send_keys("jiahui@eefocus.com")
# driver.find_element_by_id('password').send_keys("zjh112233")
# driver.find_element_by_class_name('signin').click()
# driver.find_element_by_link_text("退出").click()
driver.get("https://enterprise.bom2buy.com/user/login")
driver.set_window_size(1266, 695)
driver.find_element_by_id('email').click()
driver.find_element_by_id('email').send_keys("candicezhangjiahui@126.com")
driver.find_element_by_id("password").send_keys("zjh112233")
button_js="document.getElementsByClassName('ant-btn antd-pro-components-login-index-submit antd-pro-pages-user-login-submitButton ant-btn-primary ant-btn-lg')[0].click()"
driver.execute_script(button_js)
element = driver.find_element_by_link_text("BOM 列表")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
driver.driver.find_element_by_link_text("BOM 列表").click()
element =driver.find_element_by_css_selector("body")
actions = ActionChains(driver)
actions.move_to_element(element, 0, 0).perform()
driver.find_element_by_link_text("use Test bom").click()
driver.find_element_by_css_selector(".antd-pro-pages-bom2buy-list-list-list-header-index-bomStatus").click()
driver.find_element_by_css_selector("#state .ant-select-selection__rendered").click()
driver.find_element_by_css_selector(".ant-select-dropdown-menu-item-active").click()
driver.find_element_by_id("comment").send_keys("测试bom状态")
driver.find_element_by_css_selector(".ant-modal-footer > .ant-btn-primary").click()
element = driver.find_element_by_css_selector(".ant-modal-footer > .ant-btn-primary")
actions = ActionChains(driver)
actions.move_to_element(element).perform()
element = driver.find_element_by_css_selector("body")
actions = ActionChains(driver)
actions.move_to_element(element, 0, 0).perform()
driver.find_element_by_css_selector(".ant-table-row:nth-child(3) > .antd-pro-pages-bom2buy-list-list-engineer-index-lifecycle").click()
driver.close()





