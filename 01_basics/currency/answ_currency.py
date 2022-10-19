#!/usr/bin/env python3
kurs = int(input('Введите курс EUR/RUB: '))
kollich = int(input('Введите количество рублей: '))
summa = kollich/kurs
print(f'По курсу {kurs} на {kollich} рублей вы купите {summa:.2f} евро.')