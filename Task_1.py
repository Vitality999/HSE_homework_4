# 1 (1 балла)
# Напишите функцию calc_factorial, которая вычисляет факториал для любого неотрицательного целого числа.
import math

try:
    n = abs(int(input('Введите число\n')))

    def calc_factorial(n):
        factorial = math.factorial(n)
        return factorial
    print('Факториал числа {} ='.format(n), calc_factorial(n))

except ValueError:
    print('Вводить необходимо только целые числа!')


