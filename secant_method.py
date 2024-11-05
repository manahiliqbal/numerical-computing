import numpy as np
import sys

def f(x): return 2*x + np.cos(2*x) - (x-2)**2


n = 1
N = 100
ToL = 1e-6

p0 = float(input("Enter p0 = "))
p1 = float(input("Enter p1 = "))

while (n<=N):
    q0 = f(p0)
    q1 = f(p1)
    p2 = p1 - q1*(p1-p0)/(q1-q0)
    
    if abs(p2-p1)<=ToL:
        print(f'Root found at {p2} in {n} iterations')
        sys.exit()
    else:
        p0 = p1
        p1 = p2
        print(n, p2)
     
    n = n +1  

print('Newton Raphson method has not converged')            