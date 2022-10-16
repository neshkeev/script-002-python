#!/usr/bin/env python3
nums = []

n = int(input('Введите первое число: '))
while n:
    nums.append(n)
    n = int(input('Введите следующее число: '))

nums = sorted(nums, reverse=True)

print(f'Введённые значения в порядке убывания: ', end='')
is_first = True
for num in nums:
    if is_first:
        is_first = False
    else:
        print(', ', end='')
    print(num, end='')
print()
