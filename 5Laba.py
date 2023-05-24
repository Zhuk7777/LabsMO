import numpy as np 

def f(arg):
    #return 127/4*pow(arg,2) - 61/4*arg + 2
    return pow(arg + 1.7,2)
    
def R(N):
    return pow(0.618,N)

def calculateLN(a, b):
    return abs(a-b)

def getN(k):
    if k:
        return k+1
    else:
        return 2

def calculateY0(a0, b0):
    return a0 + ((3-pow(5,1/2))/2) *(b0-a0)

def calculateY(a, b, prevY):
    return a + b - prevY

def calculateZ(a, b, y):
    return a + b - y

def alternativeCalcZ(a, b, z):
    return a + b - z
    
def goldenRatioMethod(a, b, e):
    k = 0
    
    yPrev = calculateY0(a, b)
    zPrev = calculateZ(a, b, yPrev)
    
    f_y = f(yPrev)
    f_z = f(zPrev)
    
    while(True):
        
        if f_y <= f_z:
            b = zPrev
            zNew = yPrev
            if yPrev < zPrev:
                yNew = calculateY0(a, b)
            else:
                yNew = calculateY(a, b, yPrev)
            f_z = f_y
            f_y = f(yNew)
        else:
            a = yPrev
            if yPrev < zPrev:
                 yNew = calculateY0(a, b)
            else:
                yNew = zPrev
            #zNew = calculateZ(a, b, yPrev)
            zNew = alternativeCalcZ(a, b, zPrev)
            f_y = f_z
            f_z = f(zNew)
        
        
        N = getN(k)
        Ln = calculateLN(a,b)
        
        if Ln < e:
            return (a + b)/2, R(N)
        else:
            yPrev = yNew
            zPrev = zNew
            k+=1
            


a0 = float(input("Левая граница отрезка: "))
b0 = float(input("Правая граница отрезка: "))
e = float(input("Требуемая тоность: "))

result ,R = goldenRatioMethod(a0, b0, e)

print("Решение: ", round(result,2)) 
print("Характеристика относительного уменьшения промежутка неопределенности равна", R)