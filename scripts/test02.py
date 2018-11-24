import time

import os
from appium import webdriver

# 前置代码
# desired_caps为字典格式 - 常用参数：
desired_caps = {}
# 必填-且正确
desired_caps['platformName'] = 'Android'
# 必填-且正确
desired_caps['platformVersion'] = '5.1'
# 必填
desired_caps['deviceName'] = '192.168.56.101:5555'
# APP包名
desired_caps['appPackage'] = 'com.android.settings'
# 启动名
desired_caps['appActivity'] = '.Settings'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)
try:
    if driver.is_app_installed("com.vcooline.aike"):
        driver.remove_app("com.vcooline.aike")
        print("Remove succese!")
    else:
        driver.install_app(os.getcwd() + os.sep + "AK_CRM.apk")
        print("Install succese!")
except:
    pass
finally:
    driver.quit()
