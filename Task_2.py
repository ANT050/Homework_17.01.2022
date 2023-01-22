# Задайте список из n чисел последовательности (1 + 1/n)^n, выведеите его на экран, а так же сумму элементов списка.
# Пример:
# Для n=4 -> [2, 2.25, 2.37, 2.44]
# Сумма 9.06

def calculate_sum(n):
    list_numbers = [round(((1 + 1 / i) ** i), 2) for i in range(1, n+1)]
    total_amount = sum(list_numbers)
    return (list_numbers, total_amount)

n = int(input('\nВведите число: '))
result = calculate_sum(n)
print(f'Для n = {n} -> \033[31m{result[0]}\033[0m')
print(f'Сумма: \033[31m{result[1]}\033[0m')