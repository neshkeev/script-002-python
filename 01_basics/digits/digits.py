#!/usr/bin/env python3
num = int(input('Введите четырёхзначное число: '))

sum = num % 10 + \
    num // 10 % 10 + \
    num // 100 % 10 + \
    num // 1000 % 10

print(f'Сумма цифр равна {sum}')
