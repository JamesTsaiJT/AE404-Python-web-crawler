from selenium import webdriver
from selenium.webdriver.common.keys import Keys
import time

chrome = webdriver.Chrome()
chrome.get("https://www.google.com.tw/")
chrome.find_element_by_link_text("Gmail").click()
time.sleep(1)
chrome.find_element_by_link_text("Sign in").click()
#windows = chrome.window_handles
#chrome.switch_to_window(windows[1])
#inputBar = chrome.find_element_by_class_name("whsOnd zHQkBf")
inputBar = chrome.find_element_by_tag_name('input')
inputBar.send_keys("codingape@gmail.com")
inputBar.send_keys(Keys.ENTER)
time.sleep(1)
inputBar = chrome.find_element_by_class_name("whsOnd")
inputBar.send_keys("xxxxxxxxxxxxxxxxxxxx")
inputBar.send_keys(Keys.ENTER)


