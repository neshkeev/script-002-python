#!/usr/bin/env python3
sum = 0
k = 0

s = input('Введите первое число: ')
while s:
    n = int(s)

    sum += n
    k += 1

    s = input('Введите следующее число: ')

print(f'Среднее всех чисел: {sum / k if k > 0 else 0}')
