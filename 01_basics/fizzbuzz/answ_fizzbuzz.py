#!/usr/bin/env python3
for i in range(1, 101):
        if not i %5 and not i %3:
            print('{} FizzBuzz'.format(i)) 
        elif not i %5:
           print('{} Buzz'.format(i)) 
        elif not i %3:
           print('{} Fizz'.format(i)) 