#!/usr/bin/env python3

num = float(input('Введите целое число: '))
is_even = num % 2
print(f'Введённое число - {"не" if is_even else ""}чётное')
