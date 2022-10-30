from machinka import *

while True:
    a = input("Введите команду, для остановки завершить: ")
    if a.lower() == 'завершить':
        break
    main(a)