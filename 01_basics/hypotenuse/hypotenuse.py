#!/bin/python3

import math
line_1 = float(input("Введите длину первого катета: "))
line_2 = float(input("Введите длину второго катета: "))
print(f"Длина гипотенузы {round((math.sqrt(line_1) + math.sqrt(line_2)),2)}")
