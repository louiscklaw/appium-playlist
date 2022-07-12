import time
from time import sleep
from appium import webdriver

from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

# it's hybrid app
# idea is to switch to desired context and continue stuff there
# could be, when app redirects to url from browser (terms of agreement), etc.
# on chrome tab as separated activity unable to reproduce

desired_caps = {}
desired_caps['platformName'] = 'Android'
desired_caps['deviceName'] = 'Android'

driver = webdriver.Remote('http://192.168.10.21:4444/wd/hub', desired_caps)
driver.implicitly_wait(5)

driver.install_app("/root/apk_pool/curl.apk")
time.sleep(10)

result = driver.execute_script('mobile: shell', {
    'command': 'curl',
    'args': ['http://www.example.com'],
    'includeStderr': True,
    'timeout': 5000
})
# assert result['stdout'] == 'arg1 arg2'
print(result['stdout'])


print('done')

# time.sleep(10)
driver.quit()
