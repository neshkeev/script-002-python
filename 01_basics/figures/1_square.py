#!/usr/bin/env python3

# Введите n: 5
# *****
# *****
# *****
# *****
# *****

n = int(input('Введите n: '))

for i in range(n):
    for j in range(n):
        print('*', end='')
    print()
