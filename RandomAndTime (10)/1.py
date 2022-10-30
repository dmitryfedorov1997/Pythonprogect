# В быстрых шахматах на принятие решений для всех ходов игроку даётся 30 минут. Программа должна:
# Предлагать ввод хода (например, E2–E4) и считать потраченное время.
# После получения хода печатать оставшееся время в минутах.
# Если 30 минут закончились или игрок вводит «off» — завершать работу.
# Оформить в виде функции.

from time import *
def chess():
    Atime = 30
    while True:
         start = time()
         a = input()
         if a == 'off':
            break
         end = time()
         total = round((end - start) / 60, 2)
         Atime -= total
         print(Atime)
chess()