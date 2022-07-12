import os,sys
from pprint import pprint
from time import sleep
import base64
from os.path import dirname

from appium import webdriver
# from selenium import webdriver

CURR_DIR=os.path.abspath(os.path.dirname(__file__))
REPO_HOME=os.path.abspath(CURR_DIR+'/..')
CHROME_DRIVER_DIR=os.path.abspath(REPO_HOME+'/drivers')

VIDEO_PATH=f'{CURR_DIR}/recording'

# caps = webdriver.DesiredCapabilities.CHROME.copy()
# chrome_options = webdriver.ChromeOptions()
# mobile_emulation = {
#   "deviceName": "Nexus 5"
#   }
# chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
# chrome_options.add_argument("--headless")
# caps=chrome_options.to_capabilities()
# caps['acceptInsecureCerts'] = True
# browser = webdriver.Chrome(CHROME_DRIVER_DIR+'/chrome/86/chromedriver', desired_capabilities=caps)

caps = {
    "platformName": "Android",
    "appPackage": "com.android.chrome",
    "appActivity": "com.google.android.apps.chrome.Main",
    "automationName": "UiAutomator2",
    "clearSystemFiles":True,
    "disableWindowAnimation":True,
    "newCommandTimeout": 120,
    "fastReset": True,
    "printPageSourceOnFindFailure":True,
    "clearSystemFiles":True,
    "acceptInsecureCerts": True,
    'uiautomator2ServerLaunchTimeout': 60 * 1000
}

# This will launch your Android application.
driver = webdriver.Remote('http://192.168.10.21:4444/wd/hub', caps)

def saveRecordingScreen(driver, video_name):
  video_rawdata = driver.stop_recording_screen()

  filepath = os.path.join("{}/{}".format(VIDEO_PATH, video_name))
  with open(filepath, "wb") as vd:
      vd.write(base64.b64decode(video_rawdata))


try:
  driver.implicitly_wait(5)
  driver.start_recording_screen()

  driver.switch_to.context("NATIVE_APP")

  driver.find_element_by_id("com.android.chrome:id/terms_accept").click()
  driver.find_element_by_id("com.android.chrome:id/negative_button").click()
  driver.get('https://www.hko.gov.hk/en/gts/time/clock_e.html')
  sleep(15)

finally:
  saveRecordingScreen(driver, './helloworld.mp4')
  driver.quit()
