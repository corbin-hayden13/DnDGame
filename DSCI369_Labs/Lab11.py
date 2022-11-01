""" A function to run experiments testing matrix conditioning.
Author - Emily J. King
Date - October 15, 2021
"""
import numpy as np
from numpy import linalg as la

def matrix_cond_exp(eps):
    A = np.array([[1, 0], [0, eps]])
    try:  # I added this try-except statement so the rest of my code would execute
        return la.det(A), la.inv(A)
    except:
        return (0, 0)

# Prompt 1
# 1.a
print("1.a")
print("Input 0:", matrix_cond_exp(0))
print("Input 1:", matrix_cond_exp(1))
print("Input 1e-2:", matrix_cond_exp(1e-2))
print("Input 1e-10:", matrix_cond_exp(1e-10))
print("Input 1e-100:", matrix_cond_exp(1e-100))
print("Input 1e-1000:", matrix_cond_exp(1e-1000))
""" The only inputs that yield an error are 0 and 1e-1000 because these values equal or
      are sufficiently close to zero, and the matrix [[1, 0],[0, 0]] is not invertible,
      causing an error """

# 1.b
print("1.b")
print("Input 1e2:", matrix_cond_exp(1e2))
print("Input 1e10:", matrix_cond_exp(1e10))
print("Input 1e100:", matrix_cond_exp(1e100))
print("Input 1e1000:", matrix_cond_exp(1e1000))
""" Because there are no values equal / sufficiently close to 0, each matrix is invertible
      and produces no error """

# Prompt 2
A = np.array([[3, 1],[1, 3]])
R = np.array([[np.cos(45 * (np.pi/180)), -1 * np.sin(45 * (np.pi/180))],
              [np.sin(45 * (np.pi/180)), np.cos(45 * (np.pi/180))]])
R_inv = la.inv(R)
D = np.array([[2, 0],[0, 4]])

# 2.a
print("2.a")
print(A - (R_inv @ D @ R))  # Element [2,2] is sufficiently close to 0 for A = R_inv @ D @ R

# 2.b
print("2.b")
print("R =", R)
print("DR =", D @ R)
""" Multiplying by R rotated the square 45 degrees about the origin.
    Multiplying by DR sheered the square and rotated by 45 degrees about the origin 
    Multiplying by A sheered the square and rotated by 22.5 degrees about the origin"""

# 2.c
print("2.c")
x = np.array([[np.cos(45 * (np.pi/180))], [-1 * np.sin(45 * (np.pi/180))]])
y = np.array([[np.sin(45 * (np.pi/180))], [np.cos(45 * (np.pi/180))]])

for a in range(3):
    print(f"A^{a+1} @ x =", (A ** a+1) @ x)
    print(f"A^{a+1} @ y =", (A ** a+1) @ y)
    print()
""" Both are growing exponentially, but Ax grows much faster than Ay 
    However, Ax started much smaller, nearly 0.  A^1x also had all positive
        values whereas A^2x & A^3x had one positive and one negative value"""

# 2.d
print("2.d")
print("det(A) =", la.det(A))
print("det(D) =", la.det(D))
print("det(R) =", la.det(R))

# 2.f
""" [[0.71],[-0.71]], [[-0.71],[-0.71]], [[-0.71],[0.71]], and [[0.71],[0.71]] 
    are the unit vectors that point in the same direction as their image """
