import os, sys
sys.path.append(os.getcwd())
import base
import pytest
import allure
from base.base_action import BaseAction
from base.base_driver import init_driver
from page.search_content import SearchPage
from base.read_data import ReadData

# 解析数据
def parse_data():
    dict_data = ReadData("data.yaml").return_data()
    txt = dict_data['content']['value']
    print(txt)
    return txt


class TestSearchContent():
    def setup_class(self):
        self.driver = init_driver(base.app_package, base.app_activity)
        # BaseAction.__init__(base.app_package, base.app_activity)

    def teardown_class(self):
        self.driver.close_app()
        self.driver.quit()

    # TODO input_search ??
    # 怎么传过来？ wlan
    # 解析yaml文件
    @pytest.mark.parametrize("input_text", [parse_data()])
    # 添加注释
    @pytest.allure.step('make_some_data_foo')
    def test_search_btn(self, input_text):
        """点击搜索后点击返回"""
        search = SearchPage(self.driver)
        # 点击搜索
        search.click_search()
        # 输入搜索的内容
        search.input_search(input_text)
        # 点击返回
        search.click_back()
"""
用到的知识点：
1. PO模式
2. pytest
3. yaml文件解析和读取
4. 参数化

"""







