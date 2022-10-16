#!/usr/bin/env python3

# Введите n: 4
# *
# **
# ***
# ****

n = int(input('Введите n: '))

for i in range(n):
    for j in range(n):
        if j <= i:
            print('*', end='')
    print()
