class BaseAction:
    def __init__(self, driver):
        self.driver = driver

    def click_element(self, loc):
        """点击的基本操作"""
        self.find_element(loc).click()

    def input_element_content(self, loc, content):
        """输入框的基本操作"""
        self.find_element(loc).clear()
        self.find_element(loc).send_keys(content)

    def find_element(self, loc):
        """抽取查找元素的基本动作"""
        self.driver.implicitly_wait(10)
        return self.driver.find_element(loc[0], loc[1])

