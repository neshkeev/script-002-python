#!/usr/bin/env python3

def is_prime(num):
    if num == 1:
        return True
    for i in range(2, num):
        if num % i == 0:
            return False
    return True


if __name__ == '__main__':
    n = int(input('Введите n: '))
    print(f'Число {n} {"" if is_prime(n) else "не "}является простым')
