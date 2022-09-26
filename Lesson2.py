# 1. Напишите программу, которая принимает на вход число N и выдаёт последовательность из N членов.
#     *Пример:*
#     - Для N = 5: 1, -3, 9, -27, 81

import random as rd
#from random import randint

# n = int(input("Введите произвольное целое число: "))
# for _ in range(n):
#     print(rd.randint(-100, 100), sep=',', end=' ')


# 2. Для натурального n создать словарь индекс-значение, состоящий из элементов последовательности 3n + 1.
#     *Пример:*
#     - Для n = 6: {1: 4, 2: 7, 3: 10, 4: 13, 5: 16, 6: 19}
# print('\nЗадача 2')
# number = input("Введите число N: ")
# result = []
# for i in range(1, int(number)+1):
#     elem = [i, 3*i + 1]
#     result.append(elem)
# print(result)
# print(dict(result))

# number = input("Введите число N: ")
# result = dict()
# for i in range(1, int(number)+1):
#     result[i] = 3*i + 1
# print(result)


# 2
# print('\nЗадача 2')
# dict_numbers = {}   # Создание пустого словаря
# n = int(input('Введите число: '))
# for i in range(1, n+1):
#     dict_numbers[i] = i*3 + 1
# print(dict_numbers)

# 3. Напишите программу, в которой пользователь будет задавать две строки, а программа
#  - определять количество вхождений одной строки в другой.
print('\nЗадача 3')
str1 = input()
str2 = input()
print()
