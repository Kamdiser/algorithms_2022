"""
Задание 4.
Приведены два алгоритма. В них определяется число,
которое встречается в массиве чаще всего.
Сделайте профилировку каждого алгоритма через timeit
Обязательно напишите третью версию (здесь возможно даже решение одной строкой).
Сделайте замеры и опишите, получилось ли у вас ускорить задачу
"""
from timeit import timeit
array = [1, 3, 1, 3, 4, 5, 1]
import collections


def func_1():
    m = 0
    num = 0
    for i in array:
        count = array.count(i)
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_2():
    new_array = []
    for el in array:
        count2 = array.count(el)
        new_array.append(count2)

    max_2 = max(new_array)
    elem = array[new_array.index(max_2)]
    return f'Чаще всего встречается число {elem}, ' \
           f'оно появилось в массиве {max_2} раз(а)'


def func_3():
    m = 0
    num = 0
    for i in array:
        i = array.pop()
        count = array.count(i)+1
        if count > m:
            m = count
            num = i
    return f'Чаще всего встречается число {num}, ' \
           f'оно появилось в массиве {m} раз(а)'


def func_4():
    array = [1, 3, 1, 3, 4, 5, 1]
    counter = collections.Counter(array)
    m = counter.most_common(1)
    return f'Чаще всего встречается число {m[0][0]}, ' \
           f'оно появилось в массиве {m[0][1]} раз(а)'


print(func_1())
print(func_2())
print(func_3())
print(func_4())

print(timeit("func_1()", globals=globals(), number=1000))
print(timeit("func_2()", globals=globals(), number=1000))
print(timeit("func_3()", globals=globals(), number=1000))
print(timeit("func_4()", globals=globals(), number=1000))

# Добавил 2 варианта, последний через коллекцию, очень медленно получается.
# В третьем варианте я модернизировал первый вариант с циклом так, что при каждом цикле список сокращается
# на 1 элемент, за счет этого достигнуто снижение времени вычисления почти в 2 раза.