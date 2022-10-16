#!/usr/bin/env python3

# Введите n: 4
# ****
# ***
# **
# *

n = int(input('Введите n: '))

for i in range(n):
    for j in range(n):
        if j < n - i:
            print('*', end='')
        else:
            print(' ', end='')
    print()
