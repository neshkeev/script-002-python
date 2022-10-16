#!/usr/bin/env python3
rate = float(input('Введите курс EUR/RUB: '))
rubles = float(input('Введите количество рублей: '))
euros = rubles / rate
print(f'По курсу {rate} на {rubles} рублей вы купите {euros:.2f} евро.')
