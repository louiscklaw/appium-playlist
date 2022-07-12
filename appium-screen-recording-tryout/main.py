import os,sys
from pprint import pprint
from time import sleep
import base64

from appium import webdriver
# from selenium import webdriver


CURR_DIR=os.path.abspath(os.path.dirname(__file__))
REPO_HOME=os.path.abspath(CURR_DIR+'/..')
CHROME_DRIVER_DIR=os.path.abspath(REPO_HOME+'/drivers')

# caps = webdriver.DesiredCapabilities.CHROME.copy()

# chrome_options = webdriver.ChromeOptions()

# mobile_emulation = {
#   "deviceName": "Nexus 5"
#   }
# chrome_options.add_experimental_option("mobileEmulation", mobile_emulation)
# chrome_options.add_argument("--headless")

# caps=chrome_options.to_capabilities()
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
    'uiautomator2ServerLaunchTimeout': 60 * 1000
}

# caps['acceptInsecureCerts'] = True
# caps['uiautomator2ServerLaunchTimeout'] = 60*1000
# caps['platformName']='Android'
# browser = webdriver.Chrome(CHROME_DRIVER_DIR+'/chrome/86/chromedriver', desired_capabilities=caps)

# This will launch your Android application.
driver = webdriver.Remote('http://192.168.10.21:4444/wd/hub', caps)


VIDEO_PATH='/home/logic/_workspace/appium-playlist/appium-screen-recording-tryout/recording'

def saveRecordingScreen(driver, video_name):
  video_rawdata = driver.stop_recording_screen()

  filepath = os.path.join("{}/{}".format(VIDEO_PATH, video_name))
  with open(filepath, "wb") as vd:
      vd.write(base64.b64decode(video_rawdata))


try:

  driver.implicitly_wait(10)

  driver.start_recording_screen()

  driver.switch_to.context("NATIVE_APP")

  driver.find_element_by_id("com.android.chrome:id/terms_accept").click()
  sleep(1)

  driver.find_element_by_id("com.android.chrome:id/negative_button").click()
  sleep(1)

  driver.get('https://www.hko.gov.hk/en/gts/time/clock_e.html')
  sleep(30)

finally:
  saveRecordingScreen(driver, './helloworld.mp4')
  driver.quit()
