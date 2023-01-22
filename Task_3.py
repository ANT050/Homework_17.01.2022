# Задайте список из нескольких чисел. Напишите программу, которая найдёт сумму элементов списка, стоящих на позиции с нечетным индексом.

# Пример:

# [2, 3, 5, 9, 3] -> на нечётных позициях элементы 3 и 9, ответ: 12

from random import randint

def random_list_and_sum():
  list_numbers = [randint(1, 10) for _ in range(randint(5, 10))]
  total = sum([list_numbers[i] for i in range(1, len(list_numbers), 2)])
  print(f'\nСумму элементов списка \033[31m{list_numbers}\033[0m, стоящих на позиции с нечетным индексом: \033[31m{total}\033[0m')

random_list_and_sum()
