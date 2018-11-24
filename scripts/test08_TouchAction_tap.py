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

# 记得导包！！ 导入appium类 下的 TouchAction
# 传参记得顺序！！
# 方法1：定位元素
# wlan = driver.find_element_by_xpath("//*[@text='WLAN']")
# TouchAction(driver).tap(element=wlan).perform()
# 方法2：定位坐标
TouchAction(driver).tap(x=408,y=670).perform()

