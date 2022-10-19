#!/usr/bin/env python3
from configparser import DuplicateOptionError


fcatet = int(input('Введите длину первого катета: '))
tcatet = int(input('Введите длину второго катета: '))
dlina = fcatet**2  + tcatet**2
print(f'Длина гипотенузы {dlina}')