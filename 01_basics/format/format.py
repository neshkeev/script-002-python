#!/usr/bin/env python3
name = 'ВАСЯ'
bonus = 12345
boost = 0.12

print(f'{name.capitalize()} получил премию {bonus:_} рублей или {boost:.1%}.')
print('{} получил премию {:_} рублей или {:.1%}'.format(
    name.capitalize(), bonus, boost))
print('%s получил премию %d рублей или %.1f%%' % (
    name.capitalize(), bonus, boost*100))  # _ не получится вывести
