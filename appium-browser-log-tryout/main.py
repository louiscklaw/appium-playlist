import os,sys
from appium import webdriver
import base64
from time import sleep
import json

# GITHUB_WORKSPACE = os.environ['GITHUB_WORKSPACE']
CURR_DIR=os.path.abspath(os.path.dirname(__file__))
SCREEN_CAPTURE_DIR='{}/screens'.format(CURR_DIR)

desired_caps_A = {
  "platformName": "Android",
  "appPackage": "com.android.chrome",
  "appActivity": "com.google.android.apps.chrome.Main",
  "automationName": "UiAutomator2",
  "app":'{}/apk_pool/ApiDemos-debug.apk'.format(CURR_DIR),
  "deviceName":"emulator-5554",
  "uiautomator2ServerInstallTimeout": 2*60*1000,
  "loggingPrefs": {"browser":"ALL"},
  # "goog:loggingPrefs": {"browser":"ALL"}
}

def getScreenShot(driver, sc_filename):
  img_data = driver.get_screenshot_as_base64()
  with open(sc_filename, "wb") as fh:
    fh.write(base64.urlsafe_b64decode(img_data))

# This will launch your Android application.
driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps_A)
driver.implicitly_wait(30)
sleep(3)

context = driver.current_context
driver.switch_to.context("NATIVE_APP")
sleep(1)
driver.find_element_by_id("com.android.chrome:id/terms_accept").click()
sleep(1)

driver.find_element_by_id("com.android.chrome:id/negative_button").click()
sleep(1)


driver.get("https://aboutme.louislabs.com/")
sleep(15)

driver.switch_to.context("WEBVIEW_chrome")

fo=open('./browser.log','w')
fo.writelines(json.dumps(driver.get_log('browser')))

driver.quit()

print('done')