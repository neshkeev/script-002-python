#!/usr/bin/env python3

# Введите n: 5
# *****
# *   *
# *   *
# *   *
# *****

n = int(input('Введите n: '))

for i in range(n):
    for j in range(n):
        if 0 < i < n-1 and 0 < j < n-1:
            print(' ', end='')
        else:
            print('*', end='')
    print()
