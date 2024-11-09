import numpy as np

x = [0.8, 1, 0.7, 0.6]
y = [0.22363362, 0.65809197, 0.01375227, -0.1769446]
n = len(x)
c = float(input('Enter x: '))
yc = 0
L = np.zeros((n, 1))
for i in range(n):
    L[i] = 1
    for j in range(n):
        if j != i:
            L[i] *= (c - x[j]) / (x[i] - x[j])
    print(L[i])
    yc += y[i] * L[i]
print('For x = %.1f, y = %.10f' % (c, yc))
    