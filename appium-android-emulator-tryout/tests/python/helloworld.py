#!/usr/bin/env python3
# https://www.selenium.dev/selenium/docs/api/py/webdriver_remote/selenium.webdriver.remote.webdriver.html#module-selenium.webdriver.remote.webdriver
# https://github.com/SeleniumHQ/selenium/wiki/DesiredCapabilities
import os,sys
from pprint import pprint

import unittest

from selenium import webdriver
from selenium.webdriver.common.desired_capabilities import DesiredCapabilities

SRC_DIR=os.path.dirname(__file__)
SCREENSHOT_DIR=SRC_DIR+'/screenshot'

SELENIUM_HUB_HOST='localhost'

class GoogleTestCase(unittest.TestCase):

  def setUp(self):
    # self.browser = webdriver.Chrome()
    selenium_url = 'http://{}:4444/wd/hub'.format(SELENIUM_HUB_HOST)
    print(selenium_url)

    self.browser = webdriver.Remote(
      command_executor=selenium_url,
      desired_capabilities = {
        "platformName":"Android",
        'app': '/root/apk_pool/ApiDemos-debug.apk'
        })
    self.addCleanup(self.browser.quit)

  def testPageTitle(self):
    # self.browser.get('http://www.google.com')
    # self.assertIn('Google', self.browser.title)
    self.browser.save_screenshot('{}/hellogoogle.png'.format(SRC_DIR))

    print('done')

if __name__ == '__main__':
  unittest.main(verbosity=2)


# class GoogleTestCase(unittest.TestCase):

#   def setUp(self):
    # self.browser = webdriver.Remote(
    #   command_executor='http://127.0.0.1:4444/wd/hub',
    #   desired_capabilities = {'desired_capabilities': webdriver.DesiredCapabilities.CHROME.copy()})

#     self.addCleanup(self.browser.quit)

#   def testPageTitle(self):
#     self.browser.get('http://www.google.com')
#     self.assertIn('Google', self.browser.title)

# if __name__ == '__main__':
#   unittest.main(verbosity=2)


# # driver = webdriver.Remote(
# #    command_executor='http://127.0.0.1:4444/wd/hub',
# #    desired_capabilities=DesiredCapabilities.OPERA)

# # driver.go