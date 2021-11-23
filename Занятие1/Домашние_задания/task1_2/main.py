import datetime
import random
from collections import namedtuple

# Задачи по map
#
# Задание 1.
# Напишите программу Python, которая преобразует все символы в верхний и
# нижний регистры и удаляет повторяющиеся буквы из заданной последовательности.
# Используйте функцию map ().
# Пример:
# INPUT:  {'U', 'f', 'a', 'b', 'i', 'o', 'E'}
# OUTPUT: {('B', 'b'), ('A', 'a'), ('U', 'u'), ('I', 'i'), ('O', 'o'), ('E', 'e'), ('F', 'f')}
if __name__ == "__main__":

    def tuple_set(list_):
        return set(zip(map(str.upper, list_), map(str.lower, list_)))

    input_lst = ['U', 'f', 'a', 'b', 'i', 'o', 'E', 'e']
    print('Задание 1 \n', tuple_set(input_lst))

#
#
# Задание 2.
# Напишите программу Python для разделения заданного словаря списков на
# список словарей с помощью функции map().
#
# Пример:
# INPUT:  {"Наука": [88, 89, 62, 95], "Язык": [77, 78, 84, 80]}
# OUTPUT: [{'Наука': 88, 'Язык': 77}, {'Наука': 89, 'Язык': 78}, {'Наука': 62, 'Язык': 84}, {'Наука': 95, 'Язык': 80}]
#
    def create_dict(key, item):
        return map(lambda i: {key: i}, item)

    def task(dict_):
        n = map(create_dict, dict_, dict_.values())
        return list(map(lambda x, y: x | y, next(n), next(n)))

    input_set = {"Наука": [88, 89, 62, 95], "Язык": [77, 78, 84, 80]}

    print('Задание 2 \n', task(input_set))
#
#
#     print(task({"Наука": [88, 89, 62, 95], "Язык": [77, 78, 84, 80]}))

# Задание 3.
# Напишите скрипт для преобразования заданного списка кортежей в список строк с помощью функции map().
#
# Пример:
# Original list of tuples:
# [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
#
# Convert the said list of tuples to a list of strings:
# ['red pink', 'white black', 'orange green']
#
# Original list of tuples:
# [('Sheridan', 'Gentry'), ('Laila', 'Mckee'), ('Ahsan', 'Rivas'), ('Conna', 'Gonzalez')]
#
# Convert the said list of tuples to a list of strings:
# ['Sheridan Gentry', 'Laila Mckee', 'Ahsan Rivas', 'Conna Gonzalez']

    def zip_tuple(list_: list) -> list:
        return list(map(' '.join, list_))


    input_lst = [('red', 'pink'), ('white', 'black'), ('orange', 'green')]
    print('Задание 3 \n', zip_tuple( input_lst ))


# Задачи по лямбдам
#
# Задание 1.
# Реализуйте функцию mod_checker(x, mod=0), которая будет возвращать лямбда функцию
# от одного аргумента y, которая будет возвращать True, если остаток от деления y
# на x равен mod, и False иначе.
#
# mod_3 = mod_checker(3)
# print(mod_3(3))  True
# print(mod_3(4))  False
# mod_3_1 = mod_checker(3, 1)
# print(mod_3_1(4))  True
#
    def mod_checker(x, mod=0):
        return lambda y: y % x == mod

    print('Задание 1 lambda')
    mod_3 = mod_checker(3)
    print('mod_3', mod_3(3))
    print('mod_4', mod_3(4))
    mod_3_1 = mod_checker(3, 1)
    print('mod 3_1', mod_3_1(4))

# Задание 2.
# Напишите скрипт для сортировки списка кортежей по второму элементу с помощью Lambda.
    def sort_list_tuple(list_: list) -> list:
        return sorted(list_, key= lambda x: x[1])

    input_lst = [('red', 4), ('white', 1), ('orange', 8)]

    print('Задание 2 lambda')
    print(sort_list_tuple(input_lst))

#
# Задание 3.
# Напишите скрипт для извлечения года, месяца, даты и времени с помощью Lambda.
# В реализации исполузуйте модуль datetime.

    def get_time(key):
        dt = (datetime.datetime.now()).timetuple()
        return dt.__getattribute__('tm_'+key)


    print('Задание 3 lambda')
#так и не придумал, куда тут lamda запихать
    print(get_time('year'))
    print(get_time('mon'))


    def get_date(*args, **kwargs):
        date_ = {"year": lambda x: x.year, "month": lambda x: x.month,
                 "day": lambda x: x.day, "time": lambda x: x.time()}

        for key, kwarg in kwargs.items():
            print(key, kwarg)

        now = kwargs.get("now", datetime.datetime.now())
        print(now)

        return date_["year"](now)


    print(get_date("date", "year"))

# Задание 4.
# Напишите скрипт для сложения двух заданных списков, используя map и lambda.

    def add_2_list(lst1, lst2: list) -> list:
        return list(map(lambda x, y: x+y, lst1, lst2))

    lst1 = list(range(10))
    lst2 = list(range(11, 21))

    print('Задание 4 lambda')
    print('Исходный список 1:', lst1)
    print('Исходный список 2:', lst2)
    print('Результат поэлементного сложения:', add_2_list(lst1, lst2))

# Задание 5.
# Напишите программу Python для поиска палиндромов в заданном списке строк с помощью Lambda

    def find_poly(lst: list):
        return list(filter(lambda x: x[:] == x[::-1], lst))

    input_lst = ['Sheridan', 'потоп','Gentry', 'Laila', 'Mckee', 'Ahsan', 'Rivas', 'Conna', 'Gonzalez']

    print('Задание 5 lambda')
    print(find_poly(input_lst))

# Задание 6.
# Напишите скрипт, чтобы найти максимальное значение в заданном неоднородном списке с помощью лямбда.
# Пример списка: ['Python', 3, 2, 4, 5, 'version']

    def find_max(lst: list):
        return max(lst, key=lambda x: x if str.isdigit(str(x)) else len(x))


    print('Задание 6 lambda')
    print(find_max(['Python', 3, 2, 4, 5, 'version']))
#
# # Задание 7.
# # Напишите скрипт с использованием лямбда-выражения,
#     # чтобы проверить, отсортирован ли указанный список
#
    def check_sort(lst: list):
        return all(map(lambda x, y: x == y, lst, sorted(lst)))

    input_sort = list(range(10))
    input_unsort = list(random.randint(0, 20) for _ in range(10))

    print('Задание 7 lambda')
    print(f'На входе список: {input_sort}, результат {check_sort(input_sort)}')
    print(f'На входе список: {input_unsort}, результат {check_sort(input_unsort)}')