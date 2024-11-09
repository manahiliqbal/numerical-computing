import numpy as np
import sys

def f(x): return 2 * x * np.cos(2 * x) - (x-2) ** 2

p0 = float(input("Enter p0: "))
p1 = float(input("Enter p1: "))

if f(p0)*f(p1)>0:
    sys.exit('Function has the same sign at end points')
else:
    print('Real zero of f(x) lies between p0=', p0, ' and p1=', p1)

n = 1
N =  10
ToL = 1e-7

while n<=N:
    q0 = f(p0)
    q1 = f(p1)
    p2 = p1 - q1 * (p1 - p0) / (q1 - q0)
    q2 = f(p2)
    
    if abs(q2) <= ToL:
        print('False-position method has converged')
        print('The real zero of f(x) =', p2)
        print('Value of function at real zero =', f(p2))
        sys.exit(0)
    
    if q2 * q0 < 0:
        p1 = p2
    else:
        p0 = p2
    print('Real zero of f(x) lies between p0=', f'{p0:.10f}', ' and p1= ', f'{p1:.10f}')
    n += 1
    
print('zero not found to the desired tolerance')        

