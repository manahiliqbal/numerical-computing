import numpy as np

x = [0, 0.1, 0.3, 0.6, 1, 1.1]
y = [-6, -5.89483, -5.65014, -5.17788, -4.28172, -3.99583]

# n = len(x)
n=3

D = np.zeros((n, n))

for i in range(n):
    D[i, 0] = y[i]

for i in range(1, n):
    for j in range(1, i + 1):
        D[i, j] = (D[i, j - 1] - D[i - 1, j - 1]) / (x[i] - x[i - j])
print(D)

S = D[0, 0]
m = np.zeros((n, 1))
m[0] = 1

X = float(input('Enter x: '))
for i in range(1, n):
    m[i] = m[i - 1] * (X - x[i - 1])
    S += m[i] * D[i, i]

print('For x = %.1f, y = %.10f' % (X, S))