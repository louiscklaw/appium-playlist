import os,sys
from pprint import pprint

from appium import webdriver
from appium.webdriver.common.touch_action import TouchAction

from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait

TEST_DIR=os.path.abspath(os.path.dirname(__file__))
SCREENCAPTURE_DIR=os.path.abspath('{}/screen/zhipin-tryout'.format(TEST_DIR))

desired_caps = {
  "platformName": "Android",
  "deviceName":"nexus_5_11.0",
  "app":"/root/apk_pool/boss_11.220_c0.apk"
}
desired_caps['platformName'] = 'Android'
# desired_caps['appPackage'] = 'net.openwritings.xmtl'
# desired_caps['appActivity'] = '.MainActivity'
desired_caps['deviceName']='nexus_5_11.0'

# reference to server side
desired_caps['app'] = '/root/apk_pool/boss_11.220_c0.apk'

# This will launch your Android application.
driver = webdriver.Remote('http://localhost:4444/wd/hub', desired_caps)


print('start, louiscklaw zhipin test demo happy tour')
driver.save_screenshot('{}/zhipin_greeting_T_and_C.png'.format(SCREENCAPTURE_DIR))

ele_agree_button = driver.find_element_by_xpath(
  '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_positive"]'
)
actions = TouchAction(driver)
actions.tap(ele_agree_button)
actions.perform()

# click 我要应聘 button
# //android.widget.Button[@resource-id="com.hpbr.bosszhipin:id/btn_enter_geek"]
ele_wanted = '//android.widget.Button[@resource-id="com.hpbr.bosszhipin:id/btn_enter_geek"]'
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH , ele_wanted)))
ele_agree_button = driver.find_element_by_xpath(ele_wanted)
actions = TouchAction(driver)
actions.tap(ele_agree_button)
actions.perform()

# change country code
# //android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_country_phone_code"]
ele_wanted = '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_country_phone_code"]'
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH , ele_wanted)))
ele_agree_button = driver.find_element_by_xpath(ele_wanted)
actions = TouchAction(driver)
actions.tap(ele_agree_button)
actions.perform()

# click 852
# (//android.widget.RelativeLayout[@resource-id="com.hpbr.bosszhipin:id/rl_item"])[2]
# 中国香港
# //android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_country" and @text="中国香港"]
ele_wanted = '(//android.widget.RelativeLayout[@resource-id="com.hpbr.bosszhipin:id/rl_item"])[2]'
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH , ele_wanted)))
ele_wanted_hong_kong = '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_country" and @text="中国香港"]'
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH , ele_wanted_hong_kong)))
ele_agree_button = driver.find_element_by_xpath(ele_wanted_hong_kong)
actions = TouchAction(driver)
actions.tap(ele_agree_button)
actions.perform()

# click telephone number input, input space
# //android.widget.EditText[@resource-id="com.hpbr.bosszhipin:id/et_phone"]
ele_wanted = '//android.widget.EditText[@resource-id="com.hpbr.bosszhipin:id/et_phone"]'
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH , ele_wanted)))
ele_wanted_input = driver.find_element_by_xpath(ele_wanted)
actions = TouchAction(driver)
actions.tap(ele_wanted_input)
actions.perform()
ele_wanted_input.send_keys("91234567")


# click checkbox to agree
# //android.widget.CheckBox[@resource-id="com.hpbr.bosszhipin:id/checkbox"]
ele_wanted = '//android.widget.CheckBox[@resource-id="com.hpbr.bosszhipin:id/checkbox"]'
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH , ele_wanted)))
ele_agree_button = driver.find_element_by_xpath(ele_wanted)
actions = TouchAction(driver)
actions.tap(ele_agree_button)
actions.perform()

# click next button
# //android.widget.Button[@resource-id="com.hpbr.bosszhipin:id/btn_confirm"]
ele_wanted = '//android.widget.Button[@resource-id="com.hpbr.bosszhipin:id/btn_confirm"]'
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH , ele_wanted)))
ele_agree_button = driver.find_element_by_xpath(ele_wanted)
actions = TouchAction(driver)
actions.tap(ele_agree_button)
actions.perform()


print("waiting security scan....")
# # showing security scan
# //android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_status"]
ele_wanted = '//android.widget.TextView[@resource-id="com.hpbr.bosszhipin:id/tv_status"]'
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH , ele_wanted)))
driver.save_screenshot('{}/showing_security_scan.png'.format(SCREENCAPTURE_DIR))

print("waiting puzzle....")
# showing puzzle
# //android.view.View[@text="请完成安全验证"]
ele_wanted = '//android.webkit.WebView[@text="易盾验证码"]'
WebDriverWait(driver, 30).until(EC.presence_of_element_located((By.XPATH , ele_wanted)))
driver.save_screenshot('{}/showing_puzzle.png'.format(SCREENCAPTURE_DIR))

driver.save_screenshot('{}/done.png'.format(SCREENCAPTURE_DIR))

# print(search_box_element)

print("done")