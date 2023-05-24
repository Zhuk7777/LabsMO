import numpy as np 

def f(x1,x2):
    return (x1-2.5)**3 + (x2 + 2.5)**3
    #return 2*pow(x1,2) + pow(x2,2)

def gradient(x1,x2):
    return 3*(x1 -2.5)**2, 3*(x2 + 2.5)**2

def norm(xi):
    sum = 0.0
    for i in range(len(xi)):
        sum += pow(xi[i], 2)
    return pow(sum, 1/2)

def difference(x0,grad):
    return x0[0] - grad[0], x0[1] - grad[1]

def stepCrushingMethod(x0,e,a):
    while norm(gradient(x0[0],x0[1])) >= e:
        x1 = difference(x0, [x * a for x in gradient(x0[0],x0[1])])
        while f(x1[0],x1[1]) >= f(x0[0], x0[1]):
            a/=2
            x1 = difference(x0, [x * a for x in gradient(x0[0],x0[1])])
        x0 = x1
        
    return x0, f(x0[0],x0[1])
        

e = 0.001
x0 = np.zeros(2)
x0[0] = 0.5
x0[1] = 1
a = 1

x,f_x = stepCrushingMethod(x0,e,a)
print('x* = ', x)
print('f(x*) = ', f_x)
#print(norm(gradient(x0[0],x0[1])))
