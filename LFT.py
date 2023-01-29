import numpy as np
import matplotlib.pyplot as plt

def rotation(v, phi_case):
    x = v[0]
    y = v[1]
    z = v[2]
    #angle of rotation
    if phi_case == 0:
        phi = np.pi / 2.
    if phi_case == 1:
        phi = np.pi / 3.
    if phi_case == 2:
        phi = 2 * np.pi / 3.
    phi = -phi 
    fx = x
    fy = np.cos(phi) * y + np.sin(phi) * z
    fz = np.cos(phi) * z - np.sin(phi) * y

    return [fx, fy, fz]


def conj(v):
    return [(v[0] + v[1]) / np.sqrt(2), (-v[0] + v[1]) / np.sqrt(2), v[2]]

def conj_obr(v):
    return [(v[0] - v[1]) / np.sqrt(2), (v[0] + v[1]) / np.sqrt(2), v[2]]

def x_projection(v):
    return v[0] / (0.5 - v[2])

def y_projection(v):
    return v[1] / (0.5 - v[2])

def rev_proj(r, a):
    return [np.cos(a) * r / ( r*r + 1), np.sin(a) * r / ( r*r + 1) , r*r / (r*r + 1) - 0.5]

print('Введите номер варианта:')
n = int(input())
vector_case = n % 3
phi_case = (n - 9 * (n // 9)) //3


A = [0] * 20
R = [0] * 20
for j in range(10):
    A[j] = np.linspace(0, 2 * np.pi, 10000)
    R[j] = j
for j in range(10):
    R[10 + j] = np.linspace(0, 10, 10000)
    A[10 + j] = j * 2 * np.pi / 10.


#cases corresponds to axis of rotation
if vector_case == 0:
    for j in range(10):
        plt.plot(x_projection(rotation(rev_proj(R[j], A[j]), phi_case)), y_projection(rotation(rev_proj(R[j], A[j]), phi_case)), color = 'black')
    for j in range(10, 20):
        plt.plot(x_projection(rotation(rev_proj(R[j], A[j]), phi_case)), y_projection(rotation(rev_proj(R[j], A[j]), phi_case)), color = 'blue')
# 1 -1
if vector_case == 2:
    for j in range(10):
        plt.plot(x_projection(conj(rotation(conj_obr(rev_proj(R[j], A[j])), phi_case))), y_projection(conj(rotation(conj_obr(rev_proj(R[j], A[j])), phi_case))), color = 'black')
    for j in range(10, 20):
        plt.plot(x_projection(conj(rotation(conj_obr(rev_proj(R[j], A[j])), phi_case))), y_projection(conj(rotation(conj_obr(rev_proj(R[j], A[j])), phi_case))), color = 'blue')
# 1 1
if vector_case == 1:
    for j in range(10):
        plt.plot(x_projection(conj_obr(rotation(conj(rev_proj(R[j], A[j])), phi_case))), y_projection(conj_obr(rotation(conj(rev_proj(R[j], A[j])), phi_case))), color = 'red')
    for j in range(10, 20):
        plt.plot(x_projection(conj_obr(rotation(conj(rev_proj(R[j], A[j])), phi_case))), y_projection(conj_obr(rotation(conj(rev_proj(R[j], A[j])), phi_case))), color = 'blue')
plt.xlim([-5, 5])
plt.ylim([-5, 5])
plt.grid()
plt.show()

