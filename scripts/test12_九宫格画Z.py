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

save = driver.find_element_by_xpath("//*[@text='电池']")
more = driver.find_element_by_xpath("//*[@text='WLAN']")

driver.drag_and_drop(save,more)
time.sleep(2)
safe = driver.find_element_by_xpath("//*[@text='安全']")
safe.click()
time.sleep(2)
el1 = driver.find_element_by_xpath("//*[@text='屏幕锁定方式']")
el1.click()
time.sleep(2)
el2 = driver.find_element_by_xpath("//*[@text='图案']")
el2.click()

time.sleep(2)
TouchAction(driver).press(x=238, y=852).wait(500).move_to(x=1192-238, y=852-852).wait(500).\
    move_to(x=231-1192, y=1813-852).move_to(x=1196-231, y=0).wait(500).release().perform()
