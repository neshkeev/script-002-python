#!/usr/bin/env python3
from curses.ascii import isdigit
while True:
    a = input('Введите количество баллов: ')
    if a.isdigit():
        if int(a) in range(0, 55):
            print('Оценка 2') 
        elif int(a) in range(55, 70):
            print('Оценка 3') 
        elif int(a) in range(70, 85):
            print('Оценка 4')
        elif int(a) in range(85, 101):
            print('Оценка 5')
    else:
        break

