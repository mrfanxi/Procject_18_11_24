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
# 设置中文
desired_caps['unicodeKeyboard'] = True
desired_caps['resetKeyboard'] = True
# APP包名
desired_caps['appPackage'] = 'com.android.settings'
# 启动名
desired_caps['appActivity'] = '.Settings'

driver = webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

import base64

