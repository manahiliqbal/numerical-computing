import numpy as np
import sys

def f(x): return x + 1 - 2*np.sin(np.pi * x)

p0 = float(input("Enter p0: "))
p1 = float(input("Enter p1: "))
n = 1
N = 10
tol = 1e-7
print('n p f(p)')

while n <= N:
    q0 = f(p0)
    q1 = f(p1)
    p2 = p1 - q1 * (p1 - p0) / (q1 - q0)
    print(f'{n} \
        {p2:.10f} \
        {f(p2):.10f}')
    if abs(f(p2)) <= tol or abs(p2 - p1) <= tol:
        print('Secant method has converged')
        print('The real zero of f(x) =', p2)
        print('Value of function at real zero =', f(p2))
        sys.exit(0)
    else:
        p0 = p1
        p1 = p2
    n += 1
print('zero not found to the desired tolerance')