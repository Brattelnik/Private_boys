xinput=open('input.txt','r')
stroka=xinput.readline()
if stroka=='':
    print("Введите в файле input.txt значения по х и по у через пробел, два значения на строку, cохраните файл. После включите программу")
else:
    import numpy as np
    import matplotlib.pyplot as plt
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
    ZnachX=[]
    ZnachY=[]
    ZnachX.append(x)
    ZnachY.append(y)
    MaxX=x
    MindeltaX=x
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
            m=x
            x=float(stroka[0])
            y=float(stroka[1])
            ZnachX.append(x)
            ZnachY.append(y)
            n+=1
            if x>MaxX:
                MaxX=x
            if ((x-m)**2)**0.5<MindeltaX:
                MindeltaX=((x-m)**2)**0.5
        else:
            break
    n=n+1
    xinput.close()
    b=(proizvedeniexy/n-summax*summay/n/n)/(xkvadrat/n-summax**2/(n*n))
    a=summay/n - b*summax/n
    deltab=(1/n**0.5)*(((ykvadrat/n - (summay/n)**2)/(xkvadrat/n - (summax/n)**2))-b**2)**0.5
    deltaa=deltab*(xkvadrat/n-(summax/n)**2)**0.5
    print("Уравнение прямой имеет вид y=",a,"+",b,"x")
    print("Погрешность измерения а=",deltaa)
    print("Пoгрешность измерения b=",deltab)
    x=np.arange(0,1.1*MaxX,0.1*MindeltaX)
    plt.plot(x,a+b*x)
    plt.grid(True)
    a=a*10000//10/1000
    b=b*10000//10/1000
    deltaa=deltaa*10000//10/1000
    deltab=deltab*10000//10/1000
    plt.plot(ZnachX,ZnachY,'ro')
    plt.plot(x,0*x)
    #plt.title('Ошибка коэф.при х={};Ошибка свободного члена'.format(deltab,deltaa))
    if a>0:
        plt.title('y={}x+{}\n$\sigma_b$={}; $\sigma_a$={}'.format(b,a,deltab,deltaa))
    else:
        plt.title('y={}x{}\n$\sigma_b$={}; $\sigma_a$={}'.format(b,a,deltab,deltaa))
    plt.legend(('График функции','Экспериментальные точки'),loc='best')
    plt.show()
        
    
