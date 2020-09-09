import base
from base.base_action import BaseAction


class SearchPage(BaseAction):

    def click_search(self):
        """点击搜索按钮"""
        self.click_element(base.search_button)

    def input_search(self, text):
        """输入搜索内容"""
        self.input_element_content(base.search_edit_text, text)

    def click_back(self):
        self.click_element(base.back_button)

