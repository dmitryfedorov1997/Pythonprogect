# Очень часто веб-дизайнеры используют HEX-значение какого-либо цвета.
# Напишите программу принимающую 2 позиционных аргумента: слово "Цвета" и количество цветов.
# и произвольное количество значений Цвет : HEX. Программа должна вывести все данные на экран.

def F(cal, k, **coll):
    print(f'{cal}: {k}')
    for i in coll:
        print(f'{i}: {coll[i]}')