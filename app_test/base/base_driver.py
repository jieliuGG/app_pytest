from appium import webdriver


def init_driver(app_package, app_activity):
    desired_caps = dict()
    # 测试设备信息
    desired_caps['platformName'] = 'Android'
    desired_caps['platformVersion'] = '5.1'
    desired_caps['deviceName'] = '192.168.56.101:5555'
    # app信息
    desired_caps['appPackage'] = app_package # 抽取为常量
    desired_caps['appActivity'] = app_activity # 抽取为常量

    # 返回驱动对象
    return  webdriver.Remote('http://127.0.0.1:4723/wd/hub', desired_caps)

