# words = 'hello hello'
#
# def parser_string(words):
#     words = words.split(' ')
#     if words[0][0].upper() == words[1][0].upper():
#         print('слова начинаются одинаково')
#     else:
#         print('слова начинаются по-разному')
#
# parser_string(words)
#
# def two_number (x, y):
#     z = x+y
#     if z == 20 or x == 20 or y == 20:
#         if x == 20:
#             print('x = 20')
#         elif y == 20:
#             print('y = 20')
#         else:
#             print('z = 20')
#     return False
# two_number(1, 19)
#
#
# def reversed_string(s):
#     s = s.split(' ')
#     print(s)
#     s.reverse()
#     s = ' '.join(s)
#     print(s)
# reversed_string('a b c d')
#
# def gen():
#     yield 'hello'
#
# x = gen()
#
# print(next(x))

# list_comprehensions = [x for x in range(0, 101) if x % 5 == 0]
# print(list_comprehensions)
n = range(0, 101)
def list_comprasions(n = range(0,101)):
    for item in n:
        if item % 5 == 0:
            yield item
        else:
            return False
list_comprasions(n)

number = list_comprasions(n)
print(next(number))

# with open('stich.txt', 'r') as f:
#     for line in f:
#         line = line.replace('\n', '').replace('?', '').replace('!', '').replace('.', '')\
#         .replace(',', '').replace('“', '').replace('”', '')
#         s_line = line.split()
#
#
#         print(s_line)