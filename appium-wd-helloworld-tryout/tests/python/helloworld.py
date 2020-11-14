import os,sys
from pprint import pprint

from appium import webdriver

TEST_DIR=os.path.abspath(os.path.dirname(__file__))
SCREENCAPTURE_DIR=os.path.abspath('{}/screen'.format(TEST_DIR))

desired_caps = {}
desired_caps['platformName'] = 'Android'
# desired_caps['appPackage'] = 'net.openwritings.xmtl'
# desired_caps['appActivity'] = '.MainActivity'
desired_caps['deviceName']='nexus_5_8'

# reference to server side
desired_caps['app'] = '/root/apk_pool/ApiDemos-debug.apk'

# This will launch your Android application.
driver = webdriver.Remote('http://localhost:4444/wd/hub', desired_caps)

search_box_element = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView')

# reference to machine running the script
driver.save_screenshot('{}/capture_using_python.png'.format(SCREENCAPTURE_DIR))

print(search_box_element)
