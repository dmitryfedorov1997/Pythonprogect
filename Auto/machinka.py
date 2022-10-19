def main(input):
    if 'рас' in input.lower():
        timetable()
    if 'тре' in input.lower():
        coach()
    if 'опл' in input.lower():
        cost()
    if 'наз' in input.lower():
        nameK()
    if 'сай' in input.lower():
        site()
    if 'зап' in input.lower():
        record()


list = dict()


def timetable():
    if str(list) != '{}':
        print(list)
    else:
        print('Всё свободно')


def coach():
    print('Номер Олега - +792999999')

def cost():
    print('Опалата 1500р')


def nameK():
    print('ООО Спортзал')


def site():
    print('сайт - hardsport.com')
