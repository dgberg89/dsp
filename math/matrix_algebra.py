# Matrix Algebra

import numpy as np

a = np.matrix('1, 2, 3; 2, 7, 4')
b = np.matrix('1, -1; 0, 1')
c = np.matrix('5, -1; 9, 1; 6, 0')
d = np.matrix('3, -2, -1; 1, 2, 3')
u = np.array([6, 2, -3, 5])
v = np.array([3, 5, -1, 4])
w = np.array([1, 8, 0, 5]).reshape((4, 1))
s = 6

#1. Matrix Dimensions, Qs 1.1 - 1.6
print('Q1.1) The dimensions of Matrix A is {}'.format(a.shape))
print('Q1.2) The dimensions of Matrix B is {}'.format(b.shape))
print('Q1.3) The dimensions of Matrix C is {}'.format(c.shape))
print('Q1.4) The dimensions of Matrix D is {}'.format(d.shape))
print('Q1.5) The dimensions of Vector u is {}'.format(u.shape))
print('Q1.6) The dimensions of Vector w is {}'.format(w.shape))

#2. Vector Operations Qs 2.1 - 2.5
print('\nQ2.1) u + v = {}'.format(u + v))
print('Q2.2) u - v = {}'.format(u - v))

#Q2.3 is multiply vector by scalar s, noted by alpha in the worksheet
print('Q2.3) s * u = {}'.format(s * u))

#Q2.4 is find the dot product of u and v
print('Q2.4) u.v = {}'.format(np.dot(u, v)))

#Q2.5 is find the norm (or length or magnitude) of u
print('Q2.5) The norm (length/magnitude) of u is {0:.3f} '.format(np.linalg.norm(u)))

#3. Matrix Operations, Qs 3.1 - 3.10

#For 3.1, running print(A+C) will get you a traceback error of different dimensions.
print('\nQ3.1) Matrix A + Matrix C is not defined because the two have different dimensions, A(2x3) and C(3x2).')

#For 3.2, A-C(T) is A-C(transpose) which gives C equal dimensions to A and allows operation.
print('Q3.2) A - C(T) = {}'.format(a - c.transpose()))

#For 3.3, transpose C and multiply d by scalar 3.  Both end up with same dimensions so operation is good.
print('Q3.3) C(T) + 3D = {}'.format(c.transpose() + 3 * d))

#For Q3.4, the multiplication works since it's BA.  If it were AB, it would not work given the dimension rule for matrix multiplication.
print('Q3.4) BA = {}'.format(b*a))

#For Q3.5, BA(T) will not work since the transpose of A makes the new dimensions unable to multiply (2x2 vs 3x2)
print('Q3.5) BA(T) is not defined because the transpose of A leads to new dimensions that cannot be multiplied B(2x2) and A(T)(3x2).')
print('Q3.6) BC is not defined because of dimension rule.  2x2*3x2 dimensions have inner product rule unequal.')
print('Q3.7) CB works because of dimension rule.  C*B = {}'.format(c * b))
print('Q3.8) b**4 = b*b*b*b = {}'.format(b**4))
print('Q3.9) AA(T) works because new dimensions are 2x3 3x2.  AA(T) = {}'.format(a*a.transpose()))
print('Q3.10) D(T)D works because new dimensions are 3x2 2x3.  D(T)D = {}'.format(d.transpose() * d))
