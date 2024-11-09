import numpy as np

x = [1, 1.3, 1.6, 1.9, 2.2]
y = [0.7651977, 0.620086, 0.4554022, 0.2818186, 0.1103623]
n = len(x)

F = np.zeros((n, n))

for i in range(n):
    F[i, 0] = y[i]

h = x[1] - x[0]

X = float(input('Enter x: '))

p = (X - x[0]) / h

for i in range(1, n):
    for j in range(1, i + 1):
        F[i, j] = F[i, j - 1] - F[i - 1, j - 1]

print(F)

yp = F[0, 0]

for i in range(1, n):
    m = 1
    for j in range(i):
        m *= (p - j) / (j + 1)
    yp += m * F[i, i]

print('For x = %.1f, y = %.10f' % (X, yp))