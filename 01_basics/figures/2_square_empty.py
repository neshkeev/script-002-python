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
        if i != 0 and i != n - 1 and j != 0 and j != n - 1:
            print(' ', end='')
        else:
            print('*', end='')
    print()
