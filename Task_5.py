# Напишите программу, которая будет преобразовывать десятичное число в двоичное.
# Пример:
# 45 -> 101101
# 3 -> 11
# 2 -> 10

def transformation(decimal_num):
  binary_num = lambda num: str(bin(num))[2:]
  return binary_num

decimal_num = int(input("\nВведите число: "))
transform = transformation(decimal_num)
print(f'Результат: \033[31m{decimal_num} -> {transform(decimal_num)}\033[0m')