from selenium.webdriver.common.by import By
from src.test.common.page import Page

#封装的百度首页
class BaiDuMainPage(Page):
    local_search_input = (By.ID, 'kw')
    local_search_button = (By.ID, 'su')

    def search(self, kw):
        # 搜索功能
        self.find_element(*self.local_search_input).send_keys(kw)
        self.find_element(*self.local_search_button).click()


