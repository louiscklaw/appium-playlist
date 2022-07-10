import pytest
import stringcase
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy
from time import sleep
import random

def init_driver():
  desired_caps = {}
  desired_caps['platformName'] = 'Android'
  desired_caps['app'] = 'apk_pool/aut.apk'
  driver = webdriver.Remote('http://192.168.10.21:4444/wd/hub', desired_caps)

  return driver


def GpsOff(driver):
  result = driver.execute_script('mobile: shell', {
      'command': 'settings',
      'args': ['put', 'secure', 'location_mode', '0'],
      'includeStderr': True,
      'timeout': 5000
  })
  # assert result['stdout'] == 'arg1 arg2'
  print(result['stdout'])

def GpsOn(driver):
  result = driver.execute_script('mobile: shell', {
      'command': 'settings',
      'args': ['put', 'secure', 'location_mode', '3'],
      'includeStderr': True,
      'timeout': 5000
  })
  # assert result['stdout'] == 'arg1 arg2'
  print(result['stdout'])

def CloseApp(driver):
  return driver.close_app()

def ClearAppData(driver):
  try:
      CloseApp(driver)
      result = driver.execute_script('mobile: shell', {
          'command': 'pm',
          'args': ['clear', 'com.echk.run'],
          'includeStderr': True,
          'timeout': 5000
      })
      # assert result['stdout'] == 'arg1 arg2'
      print(result['stdout'])
  except Exception as e:
    print('ignore exception')

# https://appium.github.io/python-client-sphinx/

class TestAndroidBasicInteractions():

    def test_appium_helloworld(self):
      driver = init_driver()
      print(driver.session_id)


      try:
        # clear app data
        ClearAppData(driver)

        GpsOff(driver)
        # 觀塘地鐵站
        # driver.set_location(22.3116204,114.226004, 0)

        # 翠屏南邨
        # driver.set_location(22.3176733+random.random()/1000000,114.2293845+random.random()/1000000, 0)

        # driver.set_location(22.3172915+random.random()/100000000,114.2312236+random.random()/100000000, 0)

        # 22.3279917,114.1855221
        # 22.3161392,114.1853441
        center_pos = [22.3161392,114.1853441]
        target_pos = [center_pos[0]+(random.random()/10000), center_pos[1]+(random.random()/10000)]
        driver.set_location(target_pos[0], target_pos[1], 0)

        sleep(3)
        GpsOn(driver)


        # reset line, app reset

        # start application
        driver.activate_app('com.echk.run')
        sleep(5)

        # start test, app ready before this line

        # approximate
        # el = driver.find_element(AppiumBy.XPATH,'/hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[2]/android.widget.RadioGroup/android.widget.RadioButton[2]')
        # el.click()

        # while using app
        # /hierarchy/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.FrameLayout/android.widget.ScrollView/android.widget.LinearLayout/android.widget.LinearLayout/android.widget.LinearLayout[3]/android.widget.Button[1]
        el = driver.find_element(AppiumBy.XPATH,'//*[@resource-id="com.android.permissioncontroller:id/permission_allow_foreground_only_button"]')
        el.click()
        sleep(5)
        # driver.set_location(22.2761647046, 114.161799692, 0)


        # 明晒
        # /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.TextView

        el = driver.find_element(AppiumBy.XPATH,'//*[@text="明晒>"]')
        el.click()
        sleep(3)

        # 見到有鬼
        # /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/androidx.drawerlayout.widget.DrawerLayout/android.widget.RelativeLayout/android.widget.RelativeLayout/android.widget.RelativeLayout[2]/android.widget.ImageView
        el = driver.find_element(AppiumBy.XPATH,'//*[@resource-id="com.echk.run:id/alert"]')
        el.click()
        sleep(5)

        el = driver.find_element(AppiumBy.XPATH,'//*[@content-desc="My Location"]')
        el.click()
        sleep(5)

        # 鬼畫符
        # /hierarchy/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.LinearLayout/android.widget.FrameLayout/android.widget.RelativeLayout/android.widget.LinearLayout/android.widget.LinearLayout[1]/android.widget.ImageView
        el = driver.find_element(AppiumBy.XPATH,'//*[@resource-id="com.echk.run:id/button1"]')
        el.click()
        sleep(5)


        driver.save_screenshot('screens/helloworld.png')
        print('done')
        driver.quit()
      except Exception as e:
        assert False, e
        driver.quit()
