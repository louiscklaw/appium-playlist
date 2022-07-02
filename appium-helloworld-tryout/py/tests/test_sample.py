import pytest
from appium import webdriver

def func(x):
  return x + 1

# def test_pytest_fail():
#   assert func(3) == 5

def test_pytest_pass():
  assert func(4) == 5

class TestAndroidBasicInteractions():


    @pytest.fixture(scope='function')
    def driver(self):
      desired_caps = {}
      desired_caps['platformName'] = 'Android'
      desired_caps['app'] = 'apk_pool/ApiDemos-debug.apk'
      driver = webdriver.Remote('http://192.168.10.21:4444/wd/hub', desired_caps)

      return driver


    def test_appium_helloworld(self, driver):
      driver.save_screenshot('screens/helloworld.png')
      print('test_appium_helloworld')
