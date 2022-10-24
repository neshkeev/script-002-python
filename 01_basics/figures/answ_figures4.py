#!/usr/bin/env python3
a = int(input('Введите число n: '))
for b in range(a):
    for c in range(a):
        if c < a - b - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()