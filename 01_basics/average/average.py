#!/bin/python3

import math

my_list = []
flag = True
first_finder = input("Введите первое число: ")
while flag:
    next_finder = input("Введите следующее число: ")
    my_list.append(next_finder)
    if next_finder == "":
        flag = False
del my_list[-1]
my_list.append(first_finder)
print(round(sum(int(x) for x in my_list) / len(my_list),2))