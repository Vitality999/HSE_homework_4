# 4 (2 + 1 балл)
# 4.1 Используя функцию calc_factorial из первого задания, напишите list comprehension, который из списка чисел получает
# список факториалов.
# Пример:
# [1, 5, 20, 3, 7] -> [1, 120, 2432902008176640000, 6, 5040]
# 4.2 Не изменяя список, модифицируйте list comprehension, чтобы он пропускал числа больше 30: Пример:
# [1, 5, 20, 31, 3, 7] -> [1, 120, 2432902008176640000, 6, 5040]
import math
def calc_factorial(n):
    factorial = math.factorial(n)
    return factorial

li = [1, 5, 20, 3, 7, 30, 31, 32, 10]

list_comprehension = [calc_factorial(n) for n in li] #4.1
print(list_comprehension)
list_comprehension_mod = [calc_factorial(n) for n in li if n <= 30] #4.2
print(list_comprehension_mod)



