#!/usr/bin/env python3
name = 'вася'
bonus = 12345
boost = 0.12
print(f'{name} получил премию {bonus:_} рублей или {boost:.1%}.')
print('{} получил премию {:_} рублей или {:.1%}'.format(
    name, bonus, boost))
print('%s получил премию %d рублей или %.1f%%' % (
    name, bonus, boost*100))