# В каждом заплыве участвуют два случайных спортсмена из разных сборных. Напиши программу для печати номеров спортсменов.
# 1) Программа должна запрашивать количество спортсменов в каждой сборной с сообщением: «Число участников сборной _:».
# 2) Затем должна печататься пара случайных спортсменов из разных сборных для заплыва в формате: «Пловец _ - пловец _».

import random
a=int(input('Число участников'))
b=random.randint(1, a)
c=random.randint(1, a)
print('Пловец', b, '-', 'Пловец', c)