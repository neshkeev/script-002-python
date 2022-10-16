#!/usr/bin/env python3

def median(*numbers):
    n = len(numbers)
    if n == 0:
        return 0
    if n % 2 == 0:
        return (numbers[(n-1)//2] + numbers[n//2]) / 2
    return numbers[n//2]


assert median() == 0
assert median(1, 2, 6) == 2
assert median(1, 2, 6, 19) == 4
