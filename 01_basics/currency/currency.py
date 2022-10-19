#!/bin/python3

EUR_RUB = float(input("Введите курс EUR/RUB: "))
RUB = float(input("Введите количество рублей: "))
print(f"По курсу {EUR_RUB} на {RUB} рублей вы купите {RUB//EUR_RUB} евро.")