import numpy as np
import sys

def f(x): return 2 * x * np.cos(2 * x) - (x-2) ** 2
def fprime(x): return -4 * x * np.sin(2 * x) + 2 * np.cos(2 * x) - 2 * (x - 2)

p0 = float(input("Enter p0: "))
n = 1
N = 10
tol = 1e-7
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