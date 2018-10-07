# 5(3 балла)
# Функция open(file_name) имеет опциональный аргумент encoding, в который можно передать строкой название кодировки,
# в которой стоит открыть файл. Большинство файлов в интернете закодированно в 'utf8', но Windows для файлов,
# в которых содержится кириллица, использует кодировку 'windows-1251'.
# Скачайте файлы со стрихотворением Пушкина в разных кодировках:
# https://raw.githubusercontent.com/SlinkoIgor/data_mining_course2/master/03_functions_iterators_generators/Onegin_utf8.txt
# и https://raw.githubusercontent.com/SlinkoIgor/data_mining_course2/master/03_functions_iterators_generators/Onegin_windows1251.txt
# (скачивать нужно не копируя текст, а файл целиком. Это можно сделать, нажав правой кнопкой на страницу -> сохранить страницу)
#
# Откройте каждый из файлов в питоне, воспользовавшишь функций open(file_name, encoding='utf8')
# либо open(file_name, encoding='windows-1251') соответственно. Сделайте read и удостоверьтесь,
# что содержимое файлов полностью совпадает.

with open('Onegin_utf8.txt', 'r', encoding='utf-8') as utf:
    content_utf = utf.read()


with open('Onegin_windows1251.txt', 'r', encoding='windows-1251') as windows:
    content_windows = windows.read()

if content_windows == content_utf:
    print('Содержимое совпадает!')
else:
    print('Содержимое не совпадает!')

