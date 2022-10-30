def main(input):
    if 'рас' in input.lower():
        time()
    if 'тре' in input.lower():
        coach()
    if 'опл' in input.lower():
        cost()
    if 'сай' in input.lower():
        site()
    if 'трек' in input.lower():
        site2()

list = dict()

def time():
    if str(list) != '{}':
        print(list)
    else:
        print('Всё свободно')

def cost():
    print('Опалата 1500р')

def coach():
    print('Номер Тиньков Роман Генадьевич- +79282345679')

def site():
    print('сайт - hardsport.com')

def site2():
    print('')