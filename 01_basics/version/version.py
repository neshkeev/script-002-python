#!/usr/bin/env python3

data = "MyProgram V1.2.3 Copyright (c) 2022"

n1 = data.lower().find(' v') + 2
n2 = data.find(' ', n1)

version = data[n1:n2]

print(f'Версия: {version}')
