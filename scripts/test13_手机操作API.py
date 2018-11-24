import time
from appium import webdriver
# 前置代码
# desired_caps为字典格式 - 常用参数：
from appium.webdriver.common.touch_action import TouchAction

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
# 获取当前设备时间
print(driver.device_time)
# 获取当前手机分辨率，非宽高
print(driver.get_window_size())

# 向手机发送键
# 注意：手机的音量键按第一次时会把界面调出，是不会生效的.
for i in range(4):
    driver.keyevent(25)
    time.sleep(1)

for j in range(3):
    driver.keyevent(24)
    time.sleep(1)

