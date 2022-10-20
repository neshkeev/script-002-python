#!/bin/python3

finder = int(input("введите число : "))
i = 0
dot = '*'
if finder == 4:
    while i < 4:
        print(dot*finder) 
        i += 1
elif finder == 3:
    print(f"{dot*finder}\n{dot} {dot}\n{dot*finder}")
elif finder == 5:
    finder = 4
    print(f"{dot*finder}\n{dot}  {dot}\n{dot}  {dot}\n{dot*finder}")
elif finder == 6:
    finder = 5
    print(f"{dot*finder}\n{dot}   {dot}\n{dot}   {dot}\n{dot}   {dot}\n{dot*finder}")