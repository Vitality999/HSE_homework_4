# 3 (3 балла)
# Напишите функцию get_factorial_generator, создающую генератор для вывода последовательности из факториалов целых чисел.
# Дополните уже существующий код:
# def get_factorial_generator():
# # Ваш код здесь
# factorial_generator = get_factorial_generator()
# print(next(factorial_generator))  # печатает 1
# print(next(factorial_generator))  # печатает 1
# print(next(factorial_generator))  # печатает 2
# print(next(factorial_generator))  # печатает 6
# print(next(factorial_generator))  # печатает 24

def get_factorial_generator():
    number = abs(int(input('Введите число\n')))
    factorial = 1
    err = 'Итератор исчерпал доступные значения'
    if number > 0:
        for item in range(1, number+1):
            factorial *= item
            yield factorial
        return err
    elif number == 0:
        yield factorial
        return err

get_factorial_generator()

factorial_generator = get_factorial_generator()
print(next(factorial_generator))  # печатает 1
print(next(factorial_generator))  # печатает 2
print(next(factorial_generator))  # печатает 3
print(next(factorial_generator))  # печатает 4
print(next(factorial_generator))  # печатает 5
# и тд.


