import csv
from datetime import datetime

def _format_date(date_str):
    """Форматировать дату

    :param date_str: дата
    """    
    
    dt = datetime.strptime(date_str, "%B %d, %Y %I:%M:%S %p")
    return dt.strftime("%d %B %Y %H:%M:%S")

def generate_csv_report(transactions, filename='transactions_report.csv'):
    """Сгенерировать csv файл

    :param transactions: список транзакции
    :param filename: имя файла
    """
    
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerow(['Date', 'Amount', 'Type'])
        for transaction in transactions:
            writer.writerow([_format_date(transaction['date']), transaction['amount'], transaction['type']])
