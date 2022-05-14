from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time
chrome = webdriver.Chrome()
chrome.get("https://www.google.com.tw/")

time.sleep(0.5)
inputBar = chrome.find_element_by_class_name("gLFyf.gsfi")
#或用css_selector
#inputBar = chrome.find_element_by_css_selector ("input.gLFyf.gsfi")
inputBar.send_keys("猿創力")
time.sleep(0.5)

#利用class定位、click()點擊
#button = chrome.find_elements_by_class_name("gNO89b")[1]
#button.click()

#利用Keys直接針對inputbar按下鍵盤Enter
inputBar.send_keys(Keys.ENTER)

time.sleep(0.5)
chrome.find_element_by_partial_link_text("猿創力程式設計學校- 兒童青少年程式設計-打造未來競爭").click()
time.sleep(0.5)
chrome.maximize_window()
time.sleep(0.5)
chrome.get_screenshot_as_file('猿創力.png')
time.sleep(0.5)
chrome.close()
