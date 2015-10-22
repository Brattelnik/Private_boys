xinput=open('input.txt','r')
if xinput.readline()=='':
    print("Введите в файле input.txt значения числителя и знаменателя через пробел, два значения на строку, завершите двумя нулями и сохраните файл. После включите программу") 
else:
    import numpy as np
    import matplotlib.pyplot as plt
    stroka=xinput.readline()
    stroka=stroka.rstrip()
    stroka=stroka.split()
    i=float(stroka[0])
    u=float(stroka[1])
    proizvedenieui=0
    ikvadrat=0
    ukvadrat=0
    while (i!=0) and (u!=0):
        ikvadrat=ikvadrat + i**2
        ukvadrat=ukvadrat + u**2
        proizvedenieui=proizvedenieui + u*i
        stroka=xinput.readline()
        if stroka!='':
            stroka=stroka.rstrip()
            stroka=stroka.split()
            i=float(stroka[0])
            u=float(stroka[1])
        else:
            break
    xinput.close()    
    print('Средний квадрат числителя=',ikvadrat)
    print('Среднее произведение числителя и знаменателя=',proizvedenieui)
    print('Средний квадрат знаменателя=',ukvadrat)
    g=proizvedenieui/ikvadrat
    print('Отношение произведения и квадрата знаменателя=', proizvedenieui/ikvadrat)
    print('Занесите под корень ошибочки=',(ukvadrat/ikvadrat)- g**2)
    x=np.arange(-10,10.01,0.01)
    plt.plot(x,(proizvedenieui/ikvadrat)*x)
    plt.show()
input()
        
    
