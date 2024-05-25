from pages.base_page import BasePage
from selenium.webdriver.common.by import By

class TransactionPage(BasePage):
    """Страница транзакции"""
    
    transaction_rows = (By.CSS_SELECTOR, 'table tbody tr')

    def get_transactions(self):
        """Получить транзакции"""
        transactions = []
        rows = self.wait_elements(self.transaction_rows)
        for row in rows:
            cols = row.find_elements(By.TAG_NAME, 'td')
            transactions.append({
                'date': cols[0].text,
                'amount': int(cols[1].text),
                'type': cols[2].text
            })
        return transactions
