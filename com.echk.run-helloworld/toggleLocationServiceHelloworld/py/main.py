# https://github.com/appium/appium/tree/master/sample-code

from appium import webdriver
from time import sleep

print('hello appium')

desired_caps = {}
desired_caps['platformName'] = 'Android'
# desired_caps['app'] = 'apk_pool/aut.apk'
# desired_caps['uiautomator2ServerLaunchTimeout'] = 60*1000

# This will launch your Android application.
driver = webdriver.Remote('http://192.168.10.21:4444/wd/hub', desired_caps)

sleep(5)

# adb shell ls /
result = driver.execute_script('mobile: shell', {
    'command': 'pm',
    'args': ['list','packages'],
    'includeStderr': True,
    'timeout': 5000
})
# assert result['stdout'] == 'arg1 arg2'
print(result['stdout'])


# # adb shell ls /
# result = driver.execute_script('mobile: shell', {
#     'command': 'settings',
#     'args': ['put', 'secure', 'location_mode', '0'],
#     'includeStderr': True,
#     'timeout': 5000
# })
# print(result['stdout'])

# sleep(5)

# # adb shell ls /
# result = driver.execute_script('mobile: shell', {
#     'command': 'settings',
#     'args': ['put', 'secure', 'location_mode', '3'],
#     'includeStderr': True,
#     'timeout': 5000
# })
# print(result['stdout'])

driver.activate_app('com.echk.run')

driver.save_screenshot('screens/helloworld.png')

print('done')
driver.quit()