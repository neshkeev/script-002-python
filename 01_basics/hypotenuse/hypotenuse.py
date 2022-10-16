#!/usr/bin/env python3
import math

k1 = float(input('Введите длину первого катета: '))
k2 = float(input('Введите длину второго катета: '))
g = math.sqrt(k1**2 + k2**2)
print(f'Длина гипотенузы {g:.2f}')
