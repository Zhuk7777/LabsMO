import numpy as np
import scipy as sp
from scipy.optimize import linprog

def f(x, y):
    return (x - 4)**2 + (y - 2)**2

def validPoint(x, y):
    return (x >= 0) and (y >= 0) and ((x + y) <= 3) and ((x + 2*y) <= 4)

def getMatrixesForSimplex():
    a = [[1, 1], [1, 2]]
    b = [3, 4]
    return a, b

def grad(x):
    result = np.zeros(2)
    result[0] = 2*(x[0] - 4)
    result[1] = 2*(x[1] - 2)
    return result

def norm(x):
    sum = 0.0
    for i in range(len(x)):
        sum += pow(x[i], 2)
    return pow(sum, 1/2)

def simplex(f_x):
    a, b = getMatrixesForSimplex()
    x1 = (0, None)
    x2 = (0, None)
    res = linprog(f_x, A_ub=a, b_ub=b, bounds=(x1, x2), method='simplex', options={"disp":False})
    return res.x

def f_minimizing(alpha, xk, lk):
    return (alpha*lk[0] + xk[0] - 4)**2 + (alpha*lk[1] + xk[1] - 2)**2


def goldenRatioMethod(eps, xk, lk):
    a = 0
    b = 1
    multiplier = (3-pow(5,1/2))/2
    
    yPrev = a + multiplier *(b-a)
    zPrev = a + b - yPrev
    
    f_y = f_minimizing(yPrev, xk, lk)
    f_z = f_minimizing(zPrev, xk, lk)
    
    while(True):
        
        if f_y <= f_z:
            b = zPrev
            zNew = yPrev
            if yPrev < zPrev:
                yNew = a + multiplier *(b-a)
            else:
                yNew = a + b - yPrev
            f_z = f_y
            f_y = f_minimizing(yNew, xk, lk)
        else:
            a = yPrev
            if yPrev < zPrev:
                 yNew = a + multiplier *(b-a)
            else:
                yNew = zPrev
            #zNew = calculateZ(a, b, yPrev)
            zNew = a + b - zPrev
            f_y = f_z
            f_z = f_minimizing(zNew, xk, lk)
        
        
        Ln = abs(a-b)
        
        if Ln < eps:
            return (a + b)/2,
        else:
            yPrev = yNew
            zPrev = zNew


def linearizationMethod(xk,eps):
    flag = True
    max_count_of_iterations = 1000
    count_of_iterations = 0

    while(flag):
        gradient = grad(xk)
        x_min = simplex(gradient) #z_k
        lk = x_min - xk
        alpha = goldenRatioMethod(eps, xk, lk)
        x_prev = xk
        xk = x_prev + alpha*lk
        if(norm(grad(xk)) < eps or norm(xk - x_prev) < eps):
            flag = False
            x_result = xk
        if(count_of_iterations >= max_count_of_iterations):
            flag = False
            x_result = xk
            print("Превышено количество итераций")
        count_of_iterations = count_of_iterations + 1

    print(x_result)
        
    

x0 = np.zeros(2)
eps = 0.00000001
x0[0] = 0.0
x0[1] = 0.0

if(not validPoint(x0[0], x0[1])):
    print("Данная точка не принадлежит множеству Omega")
else:
    linearizationMethod(x0,eps)


