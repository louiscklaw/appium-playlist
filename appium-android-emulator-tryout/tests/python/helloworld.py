from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
# desired_caps['appPackage'] = 'net.openwritings.xmtl'
# desired_caps['appActivity'] = '.MainActivity'
desired_caps['deviceName']='nexus_5_7.1.1'

# reference to server side
desired_caps['app'] = '/root/apk_pool/ApiDemos-debug.apk'

# This will launch your Android application.
driver = webdriver.Remote('http://localhost:4444/wd/hub', desired_caps)

search_box_element = driver.find_element_by_xpath('/hierarchy/android.widget.FrameLayout/android.view.ViewGroup/android.widget.FrameLayout[1]/android.view.ViewGroup/android.widget.TextView')

print(search_box_element)
