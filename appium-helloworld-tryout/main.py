from appium import webdriver

desired_caps = {}
desired_caps['platformName'] = 'Android'
# desired_caps['appPackage'] = 'net.openwritings.xmtl'
# desired_caps['appActivity'] = '.MainActivity'
# desired_caps['deviceName']='nexus_5_7.1.1'

# reference to server side
desired_caps['app'] = 'apk_pool/ApiDemos-debug.apk'
desired_caps['uiautomator2ServerLaunchTimeout'] = 60*1000

# This will launch your Android application.
driver = webdriver.Remote('http://localhost:4723/wd/hub', desired_caps)

driver.save_screenshot('screens/helloworld.png')