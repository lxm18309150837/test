import page
from base.base import Base



class PageSetting(Base):
    # 点击搜索按钮
    def page_search(self):
        self.base_click(page.loc_search_btn)

    # 输入搜索值
    def page_input(self,text):
        self.base_input(page.loc_input_text,text)

    # 点击搜索返回按钮
    def page_click(self):
        self.base_click(page.loc_back_btn)
