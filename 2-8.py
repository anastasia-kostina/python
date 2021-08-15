class DivByZero(Exception):
    def __init__(self, text):
        self.txt = text


a = 10
b = 0
try:
    if b == 0:
        raise DivByZero("Деление на ноль")
    print(a / b)
except DivByZero as err:
    print(err)
