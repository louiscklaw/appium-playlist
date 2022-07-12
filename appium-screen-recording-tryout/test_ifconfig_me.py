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
desired_caps['appPackage'] = 'com.android.chrome'
desired_caps['appActivity'] = 'org.chromium.chrome.browser.ChromeTabbedActivity'

driver = webdriver.Remote('http://192.168.10.21:4444/wd/hub', desired_caps)
driver.implicitly_wait(10)

driver.find_element_by_id("com.android.chrome:id/terms_accept").click()
driver.find_element_by_id("com.android.chrome:id/negative_button").click()

driver.get('http://ifconfig.me')
time.sleep(2)
contexts = driver.contexts

for context in contexts:
    print(context)

driver.switch_to.context("WEBVIEW_chrome")
driver.implicitly_wait(10)

# temp = driver.find_element_by_xpath('//body').text
# temp = driver.find_element_by_xpath('//*[@id="container"]').text
WebDriverWait(driver, 10).until(EC.presence_of_element_located((By.XPATH, '//*[@id="container"]')))

print("see ?")
print(temp)

# time.sleep(10)
driver.quit()
