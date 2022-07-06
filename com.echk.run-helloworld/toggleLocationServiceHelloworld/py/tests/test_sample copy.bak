import pytest
import stringcase
from appium import webdriver
from appium.webdriver.common.appiumby import AppiumBy

# def func(x):
#   return x + 1

# def test_pytest_fail():
#   assert func(3) == 5

# def test_pytest_pass():
#   assert func(4) == 5

def init_driver():
  desired_caps = {}
  desired_caps['platformName'] = 'Android'
  desired_caps['app'] = 'apk_pool/ApiDemos-debug.apk'
  driver = webdriver.Remote('http://192.168.10.21:4444/wd/hub', desired_caps)

  return driver

class TestAndroidBasicInteractions():

    # def test_tap_accesibility_helloworld(self):
    #   driver = self.init_driver()
    #   try:
    #     el = driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@content-desc="Accessibility"]')
    #     el.click()
    #     driver.save_screenshot('screens/tap_accessibility_helloworld.png')
    #     driver.quit()
    #   except Exception as e:
    #     driver.quit()

    def test_tap_accesibility_deep_helloworld(self):
      driver = init_driver()
      try:
        el = driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@content-desc="Accessibility"]')
        el.click()

        xpaths = [
          'Accessibility Node Provider',
          'Accessibility Node Querying',
          'Accessibility Service',
          'Custom View',
        ]
        for xpath in xpaths:
          el = driver.find_element(AppiumBy.XPATH, f'//android.widget.TextView[@content-desc="{xpath}"]')
          el.click()
          filename = 'screens/'+stringcase.snakecase(xpath)+'.png'
          driver.save_screenshot(filename)
          driver.back()

        driver.quit()
      except Exception as e:
        driver.quit()


    def test_tap_accesibility_helloworld(self):
      driver = init_driver()
      try:
        el = driver.find_element(AppiumBy.XPATH,'//android.widget.TextView[@content-desc="Accessibility"]')
        el.click()
        driver.save_screenshot('screens/tap_accessibility_helloworld.png')
        driver.quit()
      except Exception as e:
        driver.quit()


    def test_appium_helloworld(self):
      driver = init_driver()
      try:
        driver.save_screenshot('screens/helloworld.png')
        driver.quit()
      except Exception as e:
        driver.quit()
