# -*- coding: utf-8 -*-
import matplotlib.pyplot as plt
from math import sin, pi, radians, cos, sqrt, acos, asin, atan
import numpy as np
import copy

v_0 = 0.1  # м/с
alpha = -pi / 6  # угол между вектором скорости и x
x_0 = 0  # м
y_0 = 5  # м
m = 0.0001  # кг
q = 0.001  # Кл
Q = 0.07  # Кл
eps_0 = 8.85 * 10 ** (-12)
k = 1 / (4 * pi * eps_0)  # коэффициент


dt = 0.001
lT = [0]
lX = [x_0]
lY = [y_0]


lYPrim = [v_0 * sin(alpha)]


def x_second(x, y):
    return -(k * q * Q / m) * x * ((x ** 2 + y ** 2) ** (-3 / 2))


def y_second(x, y):
    return -(k * q * Q / m) * y * ((x ** 2 + y ** 2) ** (-3 / 2))



def XprimSuiv(x_first, XSecond, dt):
    return x_first + dt * XSecond


def YprimSuiv(y_first, YSecond, dt):
    return y_first + dt * YSecond



def XSuiv(X, x_first, dt):
    return X + dt * x_first


def YSuiv(Y, y_first, dt):
    return Y + dt * y_first



def tSuiv(t, dt):
    return t + dt


def constructor(lT, lX, lXPrim, lY, lYPrim, alpha):
    for i in range(100):
        lT.append(tSuiv(lT[-1], dt))
        lX.append(XSuiv(lX[-1], lXPrim[-1], dt))
        lY.append(YSuiv(lY[-1], lYPrim[-1], dt))
        lXPrim.append(XprimSuiv(lXPrim[-1], x_second(lX[-1], lY[-1]), dt))
        lYPrim.append(YprimSuiv(lYPrim[-1], y_second(lX[-1], lY[-1]), dt))
    return lT, lX, lXPrim, lY, lYPrim





lXPrim_1 = [v_0 * cos(alpha)]


Tuple = constructor(lT, lX, lXPrim_1, lY, lYPrim, alpha)

#plt.axis([-2, 20, -1, 25])
# добавляем подписи к осям и заголовок диаграммы
plt.xlabel('w, рад/c', fontsize=16)
plt.ylabel('v, м/c', fontsize=16)
plt.title('Множество значений')

plt.plot(Tuple[1], Tuple[3])

plt.grid(which='major')
plt.show()
