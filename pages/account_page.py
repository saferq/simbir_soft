from selenium.webdriver.common.by import By
from .base_page import BasePage
import time

class AccountPage(BasePage):
    """Страница аккаунта"""
    
    deposit_tab = (By.CSS_SELECTOR, "[ng-click='deposit()']")
    withdraw_tab = (By.CSS_SELECTOR, "[ng-click='withdrawl()']")
    transactions_tab = (By.CSS_SELECTOR, "[ng-click='transactions()']")

    deposit_input = (By.CSS_SELECTOR, "[ng-submit='deposit()'] input")
    withdraw_input = (By.CSS_SELECTOR, "[ng-submit='withdrawl()'] input")
    deposit_btn = (By.XPATH, "//button[text()='Deposit']")
    withdraw_btn = (By.XPATH, "//button[text()='Withdraw']")

    balance_text = (By.CSS_SELECTOR, "[ng-hide='noAccount'] strong:nth-child(2)")
    msg_transaction = (By.CSS_SELECTOR, ".error[ng-show='message']")
    
    

    def open_deposit_tab(self):
        """Открыть вкладку депозита"""
        
        self.click_element(self.deposit_tab)
        self.wait_element(self.deposit_input)
        self.wait_element(self.deposit_btn)

    def open_withdraw_tab(self):
        """Открыть вкладку снятия"""
        
        self.click_element(self.withdraw_tab)
        self.wait_element(self.withdraw_input)
        self.wait_element(self.withdraw_btn)
    

    def open_transactions(self):
        """Открыть вкладку транзакции"""
        
        time.sleep(3)
        self.click_element(self.transactions_tab)
    
    def deposit(self, amount: str):
        """Положить деньги на счет

        :param amount: сумма
        """
        
        self.input_text(self.deposit_input, amount)
        self.click_element(self.deposit_btn)
        self.wait_element(self.msg_transaction)

    def withdraw(self, amount: str):
        """Снять деньги со счета

        :param amount: сумма
        """
        
        self.input_text(self.withdraw_input, amount)
        self.click_element(self.withdraw_btn)
        self.wait_element(self.msg_transaction)

    def get_balance(self):
        """Получить размер баланса"""
        
        balance = self.wait_element(self.balance_text).text
        return int(balance)
