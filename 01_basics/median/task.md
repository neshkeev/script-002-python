
# Медиана

Напишите функцию, которая принимает произвольное число параметров и вычисляет медиану:

> Медианой набора {11, 9, 3, 5, 5} является число 5, так как оно стоит в середине этого набора после его упорядочивания: {3, 5, 5, 9, 11}. Если в выборке чётное число элементов, считать медианой полусумму двух соседних значений (то есть медиану набора {1, 3, 5, 7} принимают равной 4).

Для проверки работоспособности функции используйте следующий код:

```python
assert median() == 0
assert median(1, 2, 6) == 2
assert median(1, 2, 6, 19) == 4
```
