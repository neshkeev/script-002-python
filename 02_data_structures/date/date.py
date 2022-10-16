#!/usr/bin/env python3

d = input('Введите дату: ')
# d = '12-31-2000'

parts = d.split('-')

d2 = '.'.join([parts[2], parts[0], parts[1]])
print(f'Преобразованная дата: {d2}')
