import os
import sys
sys.path.append(os.getcwd())


import pytest
from base.get_driver import get_driver
from page.page_setting import PageSetting


class TestSearch():

    # 实例化页面对象
    def setup_class(self):
        self.search=PageSetting(get_driver())

    # 关闭驱动
    def teardown_class(self):
        self.search.driver.quit()

    # 根据测试步骤调用page
    @pytest.mark.parametrize("text",["123"])
    def testsearch(self,text):
        # 点击搜索
        self.search.page_search()
        # 输入123
        self.search.page_input(text)
        # 点击返回
        self.search.page_click()
        
    def test_o1(self):
        print(hahaahah)
