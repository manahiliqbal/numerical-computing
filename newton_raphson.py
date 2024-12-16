import numpy as np
import sys

def f(x): return 3*x+np.sin(x)-np.e**(x)
def fprime(x): return 3+np.cos(x)-np.e**(x)

p0 = float(input("Enter p0: "))
n = 1
N = 10
tol = 1e-9
print('n pn f(pn)')

while n <= N:
    a = f(p0)
    b = fprime(p0)
    p = p0 - a / b
    print(f'{n} \
        {p:.10f} \
        {f(p):.10f}')
    if abs(f(p)) <= tol:
        print('Newton method has converged')
        print('final p =', p)
        print('final f(p) =', f(p))
        sys.exit(0)
    else:
        p0 = p
    n += 1
    
print('zero not found to the desired tolerance')       