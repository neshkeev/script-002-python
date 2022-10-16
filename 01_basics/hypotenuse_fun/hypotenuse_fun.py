#!/usr/bin/env python3
import math


def hypotenuse(k1, k2):
    return math.sqrt(k1**2 + k2**2)


k1 = float(input('Введите длину первого катета: '))
k2 = float(input('Введите длину второго катета: '))
g = hypotenuse(k1, k2)
print(f'Длина гипотенузы {g:.2f}')
