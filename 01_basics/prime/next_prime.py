#!/usr/bin/env python3
from prime import is_prime


def next_prime(num):
    num += 1
    while not is_prime(num):
        num += 1
    return num


if __name__ == '__main__':
    n = int(input('Введите n: '))
    print(
        f'Следующее простое число после {n} это {next_prime(n)}')
