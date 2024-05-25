from datetime import datetime

def _fibonacci(n):
    """Вычислить N-е число Фибоначчи,

    :param n: число
    """
    
    if n <= 0:
        return 0
    elif n == 1:
        return 1
    else:
        a, b = 0, 1
        for _ in range(2, n + 1):
            a, b = b, a + b
        return b

def current_day_fibonacci():
    """Вычислить N-е число Фибоначчи, на текущий день """    
    
    today = datetime.today().day
    n = today + 1
    return _fibonacci(n)
