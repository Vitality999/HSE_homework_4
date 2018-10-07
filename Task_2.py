# 2 (1 балл)
# Напишите функцию для нахождения максимума из 3-х аргументов. Не пользуйтесь втроенными функциям Питона

a = float(input('Введите аргумент a\n'))
b = float(input('Введите аргумент b\n'))
c = float(input('Введите аргумент c\n'))

def max_argument(a, b, c):
    """поиск максимального аргумента"""
    if b <= a >= c:
        return a
    elif a <= b >= c:
        return b
    elif a <= c >= b:
        return c
print('Максимальный аргумент:', max_argument(a, b, c))

