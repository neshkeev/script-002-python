#!/usr/bin/env python3

score = int(input('Введите количество баллов: '))

if score >= 85:
    grade = 5
elif score >= 70:
    grade = 4
elif score >= 55:
    grade = 3
else:
    grade = 2

print(f'Оценка {grade}')
