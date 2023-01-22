# Задайте список из вещественных чисел. Напишите программу,
# которая найдёт разницу между максимальным и минимальным значением дробной части элементов, отличной от 0.
# Пример:
# [1.1, 1.2, 3.1, 5, 10.01] => 0.19

numbers = [1.1, 1.2, 3.1, 5, 10.01]

# Нахождение дробной части каждого числа
fractional_part = list(map(lambda x: x - int(x), numbers))

# Использование фильтра удаления 0
filtered_part = list(filter(lambda x: x != 0, fractional_part))

# Нахождение минимальных и максимальных значений
max_number = max(filtered_part)
min_number = min(filtered_part)

# Нахождение разницы
difference = abs(max_number - min_number)
print(f'\nРазница между максимальным и минимальным значением дробной части: \033[31m{difference}\033[0m')