#!/usr/bin/env python3

souvenirs = int(input('Введите количество сувениров: '))
trinkets = int(input('Введите количество безделушек: '))
weight = souvenirs * 75 + trinkets * 112
print(f'Общий вес посылки равен {weight} грамм')
