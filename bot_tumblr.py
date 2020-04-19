from selenium import webdriver
import os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.chrome.options import Options
from time import sleep
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support.ui import Select
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import NoSuchElementException
import time
import random
import logging
import time
import sys
import pyperclip
from pynput.keyboard import Key, Controller

keyboard = Controller()

#opening browser
chrome_options = webdriver.ChromeOptions()
prefs = {"profile.default_content_setting_values.notifications" : 2}
chrome_options.add_experimental_option("prefs", prefs)
chrome_options.add_argument("--disable-notifications")
chrome_options.add_argument("--disabled-new-style-notification")
chrome_options.add_argument("--disable-popup-blocking")
chrome_options.add_argument("test-type")

chrome_options.add_extension("path/to/extension/extension.crx")
driver = webdriver.Chrome("path/to/chromedriver", options=chrome_options)
#adding custom filters to uBlock
print("Updating filters")
driver.get('chrome-extension://cjpalhdlnbpafiamejdnhcphjbkeiagm/dashboard.html')
filters_button = driver.find_element_by_xpath("//*[text()='My filters']").click()
filePath = 'path-to/@addons/ublock_filters.txt'
with open(filePath) as readFile:
    for cnt, line in enumerate(readFile):
        lineCopied = "{}".format(line)
        pyperclip.copy(lineCopied)
        text = lineCopied.split('\n')
        text = pyperclip.paste()
        time.sleep(1)
        keyboard.press(Key.ctrl.value)
        keyboard.press('v')
        keyboard.release('v')
        keyboard.release(Key.ctrl.value)
        keyboard.press(Key.enter.value)
        keyboard.release(Key.enter.value)
        time.sleep(1)
time.sleep(2)
keyboard.press(Key.ctrl.value)
keyboard.press('s')
keyboard.release('s')
keyboard.release(Key.ctrl.value)
time.sleep(2)
print("Filters updated")
driver.get('http://www.tumblr.com/login')
print("Opened tumblr...")
time.sleep(5)

#passing login and password
email = driver.find_element_by_xpath("//input[@id='signup_determine_email']")
#+++++++++++++++++++++++++++    email here    ++++++++++++++++++++++++++++
email.send_keys('account.name@mail.com')
#+++++++++++++++++++++++++++    email here    ++++++++++++++++++++++++++++
print("Email Id entered...")
e_next  = driver.find_element_by_xpath("//span[@class=\"signup_determine_btn active\"]")
e_next.click()
time.sleep(5)

#choosing verification using password
e_vrf  = driver.find_element_by_class_name('forgot_password_link')
e_vrf.click()
driver.implicitly_wait(5)

#passing password
e_pwd = driver.find_element_by_xpath("//input[@id='signup_password']")
e_pwd.send_keys('password')
print("Password entered...")

#logging in & delay 5s
enterKey = driver.find_element_by_id("signup_password")
enterKey.send_keys(Keys.ENTER)
print("tumblr opened")

#posting with XXs delay
filePath = 'path-to/tumblr_autopost/links.txt'
with open(filePath) as readFile:
    for line in enumerate(readFile):
        driver.get("https://www.tumblr.com")
        postLink = WebDriverWait(driver, 20).until(EC.element_to_be_clickable((By.XPATH, '//button[text()="Link"]')))
        postLink.click()
        print("Post link window opened")
    #paste into text area
        time.sleep(5)
        lineCopied = "{}".format(line)
        trimmedStatus = (lineCopied[lineCopied.find("h"):-4])
        pyperclip.copy(trimmedStatus)
        newStatus = trimmedStatus.split('\n')
        newStatus = pyperclip.paste()
        print("Link to paste prepared")
        print(newStatus)
        print("Pasting new link")
        keyboard.press(Key.ctrl.value)
        keyboard.press('v')
        keyboard.release('v')
        keyboard.release(Key.ctrl.value)
        time.sleep(5)
        print("Status pasted")
        keyboard.press(Key.ctrl.value)
        keyboard.press('v')
        keyboard.release('v')
        keyboard.release(Key.ctrl.value)
        print("Description pasted")
        keyboard.press(Key.tab.value)
        keyboard.release(Key.tab.value)
        keyboard.press(Key.ctrl.value)
        keyboard.press('v')
        keyboard.release('v')
        keyboard.release(Key.ctrl.value)
        print("Tag pasted")
        time.sleep(2)
        keyboard.press(Key.tab.value)
        keyboard.release(Key.tab.value)
        keyboard.press(Key.tab.value)
        keyboard.release(Key.tab.value)
        keyboard.press(Key.enter.value)
        keyboard.release(Key.enter.value)
        time.sleep(17)
        print("Posting", "{}".format(line), "done")
print("Finished.")
