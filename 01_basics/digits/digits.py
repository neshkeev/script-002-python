#!/bin/python3

digit = str(input("Введите число: "))
finder = 0
my_list = [int(i) for i in digit]
for element in range(0, len(my_list)):
    finder = finder + my_list[element]
print(f"Сумма цифр равна {finder}")