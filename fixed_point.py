import numpy as np
import sys

def g(x): return 2-np.e**(x)+(x**2)-(3*x)

p0 = float(input("Enter p0: "))
n = 1
N = 20
TOL = 1e-2
print('n pn')

while n <= N:
    p = g(p0)
    print(f'{n} \
        {p:.15f} ')
    if abs(p - p0) <= TOL:
        print('Fixed-Point has converged')
        print('final p =', p)
        sys.exit(0)
    else:
        p0 = p
    n += 1
    
print('zero not found to the desired tolerance')          

