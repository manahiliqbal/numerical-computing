import numpy as np
import sys

def f(x): return x**2 - 6


n = 1
N = 100
ToL = 1e-9

p0 = float(input("Enter p0 = "))
p1 = float(input("Enter p1 = "))

while (n<=N):
    q0 = f(p0)
    q1 = f(p1)
    p2 = p1 - q1*(p1-p0)/(q1-q0)
    q2 = f(p2)
    
    if abs(p2-p1)<=ToL or abs(q2)<=ToL:
        print(f'Root found at {p2} in {n} iterations')
        sys.exit()
        
    else:
        p0 = p1
        p1 = p2
        print(n, p2)
     
    n = n + 1  
    
print('Secant method has not converged')            