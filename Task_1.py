# Напишите программу, которая принимает на вход вещественное число и показывает сумму его цифр. 

# Пример: 
# 6782 -> 23
# 0,56 -> 11

def sum_of_digits(num):
    return sum([int(d) for d in str(num) if d.isdigit()])

num = input("\nВведите число: ")
num = num.replace(",", ".")
num = float(num)
result = sum_of_digits(num)
print(f"Результат: \033[31m {num} -> {result}\033[0m")
