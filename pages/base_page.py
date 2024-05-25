from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC

class BasePage:
    """Базовая страница"""
    
    def __init__(self, driver):
        self.driver = driver
        self.wait = WebDriverWait(self.driver, 10)

    def click_element(self, locator):
        """Клик по элементу"""
        
        return self.wait.until(EC.element_to_be_clickable(locator)).click()


    def wait_element(self, locator):
        """Проверка отображения элемента"""
        
        return self.wait.until(EC.visibility_of_element_located(locator))


    def wait_elements(self, locator):
        """Проверка отображения элементов"""
        
        return self.wait.until(EC.visibility_of_all_elements_located(locator))
    
    def select_item_dropdown(self, item_text):
        """Выбрать из выпадающего списка"""
        
        item = (By.XPATH, f"//option[text()='{item_text}']")
        self.click_element(item)
    
    
    def input_text(self, locator, text):
        """Ввести текст в поле ввода"""
        
        item = self.wait_element(locator)
        item.click()
        item.send_keys(text)