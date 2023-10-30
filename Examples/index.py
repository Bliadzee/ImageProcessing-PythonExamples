import numpy as np

print("\n\n CREATING MATRIX WITH PYTHON \n\n")

A = [[1, 4, 5], [-5, 8, 9], [6, 8, 10], [0, 2, 38]] # iç içe liste

print("A = ", A)
print("A[1] = ", A[1])
print("A[1][2] = ", A[1][2])
print("A[0][-1] = ", A[0][-1])

# Creating martix with numpy library

print("\n\n CREATING MATRIX WITH NUMPY LIBRARY \n\n")

a = np.array([[1, 4, 5], [-5, 8, 9], [6, 8, 10], [0, 2, 38]])

print("type: ", type(a))
print("a =", "\n", a, "\n")
print("a[1] = ", a[1])
print("a[1][2] = ", a[1][2])
print("a[0][-1] = ", a[0][-1])

print("\n\n")