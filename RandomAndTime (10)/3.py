# На летней универсиаде будет проводиться по два забега. Чтобы соревнования были честными,
# участники должны распределяться между забегами случайным образом.
# Напишите программу, печатающую случайные номера забегов (1 или 2) до тех пор, пока не будет введено «off».
# После генерации каждого номера должно печататься:
# 1) «Ваш номер: _».
# 2) «Участников в первом забеге: _», «Участников во втором забеге: _».

from random import randint
a=int(input('Введите общее число участников'))
while a!=0:
    b=randint(1, a)
    print('Ваш номер', b)
    c=randint(1, a)
    d=a-c
    print('Участников в первом забеге', d, 'Участников во втором забеге', c)
    break