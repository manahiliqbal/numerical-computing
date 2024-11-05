import numpy as np
import sys

def f(x): return x**2-6
def fp(x): return 2*x

n = 1
N = 100
ToL = 1e-6

p0 = float(input("Enter p0 = "))
while (n<=N):
    p = p0 - f(p0)/fp(p0)
    
    if abs(p-p0)<=ToL:
        print(f'Root found at {p} in {n} iterations')
        sys.exit()
    else:
        p0 = p

print('Newton Raphson method has not converged')            