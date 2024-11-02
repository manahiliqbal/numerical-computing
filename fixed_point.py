import numpy as np
import sys 

def f(x): 
    return ((x + 3)/(x**2 + 2))**1/2
    

n = 1
N = 100
p0 = float(input("Enter P0: "))
ToL = 1e-5
while (n<=N):
    p = f(p0)
    
    if abs(p-p0) <= ToL:
        print(f"root found at {p} on {n}th iteration")
        sys.exit()
    else:
        p0 = p
        print (n, p) 
    n = n + 1    
        
print("Fixed point has not converged")          

