import allure
from pages.login_page import LoginPage
from pages.account_page import AccountPage
from pages.transaction_page import TransactionPage
from utils.fibonacci import current_day_fibonacci
from utils.report import generate_csv_report

@allure.feature('Banking Operations')
def test_bank_operations(driver):
    
    url = "https://www.globalsqa.com/angularJs-protractor/BankingProject/#/login"
    fib_number = current_day_fibonacci()
    
    login_page = LoginPage(driver)
    account_page = AccountPage(driver)
    transaction_page = TransactionPage(driver)
    
    with allure.step("Авторизация"):
        login_page.open_page(url)
        login_page.select_login('Harry Potter')

    with allure.step('Положим деньги на депозит'):
        account_page.open_deposit_tab()
        account_page.deposit(fib_number)
        balance = account_page.get_balance()
        assert balance == fib_number

    with allure.step('Снимим деньги с депозита'):
        account_page.open_withdraw_tab()
        account_page.withdraw(fib_number)
        balance = account_page.get_balance()
        assert balance == 0

    with allure.step('Проверяем транзакции'):
        account_page.open_transactions()
        transactions = transaction_page.get_transactions()
        assert len(transactions) == 2
        assert transactions[0]['amount'] == fib_number
        assert transactions[0]['type'] == 'Credit'
        assert transactions[1]['amount'] == fib_number
        assert transactions[1]['type'] == 'Debit'

    with allure.step('Добавляем в отчет csv фаил'):
        generate_csv_report(transactions)
        allure.attach.file('transactions_report.csv', attachment_type=allure.attachment_type.CSV)
