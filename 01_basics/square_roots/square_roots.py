#!/usr/bin/env python3
import math

a = float(input('Введите a: '))
b = float(input('Введите b: '))
c = float(input('Введите c: '))

d = b**2 - 4*a*c
if d < 0:
    print('Корней нет')
elif d == 0:
    x = -b / 2 / a
    print(f'x = {x}')
else:
    x1 = (-b + math.sqrt(d)) / 2 / a
    x2 = (-b - math.sqrt(d)) / 2 / a
    print(f'x1 = {x1}')
    print(f'x2 = {x2}')
