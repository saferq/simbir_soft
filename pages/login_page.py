
from .base_page import BasePage
from selenium.webdriver.common.by import By

class LoginPage(BasePage):
    """Страница авторизации"""
    
    customer_btn = (By.XPATH, "//button[text()='Customer Login']")
    select_btn = (By.ID, "userSelect")
    login_btn = (By.XPATH, "//button[text()='Login']")
    
    def open_page(self, url):
        """Проверка загрузки страницы"""
        
        self.driver.get(url)
        self.wait_element(self.customer_btn)

    def select_login(self, username):
        """Выбрать логин"""
        
        self.click_element(self.customer_btn)
        self.click_element(self.select_btn)
        self.select_item_dropdown(username)
        self.click_element(self.login_btn)
