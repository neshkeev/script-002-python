#!/usr/bin/env python3
a = int(input('Введите число n: '))
for b in range(a):
    for c in range(a):
        if b != 0 and b != a - 1 and c != 0 and c != a - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()