xinput=open('input.txt','r')
if xinput.readline()=='':
    print("Введите в файле input.txt значения числителя и знаменателя через пробел, два значения на строку, завершите двумя нулями и сохраните файл. После включите программу") 
else:
    import numpy as np
    import matplotlib.pyplot as plt
    stroka=xinput.readline()
    stroka=stroka.rstrip()
    stroka=stroka.split()
    x=float(stroka[0])
    y=float(stroka[1])
    proizvedeniexy=0
    ykvadrat=0
    xkvadrat=0
    summax=0
    summay=0
    n=1
    while (y!=0) and (x!=0):
        xkvadrat=xkvadrat + x**2
        ykvadrat=ykvadrat + y**2
        summax+=x
        summay+=y
        proizvedeniexy=proizvedeniexy + x*y
        stroka=xinput.readline()
        if len(stroka)>1:
            stroka=stroka.rstrip()   
            stroka=stroka.split() 
            x=float(stroka[0])
            y=float(stroka[1])
            n+=1
        else:
            break
    n=n+1
    print(n)
    xinput.close()    
    b=(proizvedeniexy/n-summax*summay/n/n)/(xkvadrat/n-summax**2/(n*n))
    a=summay/n - b*summax/n
    deltab=(1/n**0.5)*(((ykvadrat/n - (summay/n)**2)/(xkvadrat/n - (summax/n)**2))-b**2)**0.5
    deltaa=deltab*(xkvadrat/n-(summax/n)**2)**0.5
    print("Уравнение прямой имеет вид y=",a,"+",b,"x")
    print("Погрешность измерения а=",deltaa)
    print("ПОгрешность измерения b=",deltab)
    x=np.arange(0,10.01,0.01)
    plt.plot(x,a+b*x)
    plt.show()
        
    
