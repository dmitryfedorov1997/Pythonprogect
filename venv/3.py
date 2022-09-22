
#Eda = input("Введите: завтрак, плотно, либо ничего")
#if Eda == ("завтрак"):
#    print("Каша")
#elif Eda == ("плотно"):
#    print("Плов")
#else:
#    print( "Котлета с пюре" )

Sum = int(input("Сумма к оплате"))
Time = int(input("Время"))
if Time>=8 and Time<=22:
    if Time>=10 and Time<=12:
        print(Sum / 2)
        if Time>=20 and Time<=22:
            print(Sum / 4)
else:
    print("Акция не действует")

