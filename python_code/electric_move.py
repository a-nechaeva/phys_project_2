from math import *
import matplotlib.pyplot as plt


# ---- начальные условия ---- #
v_0 = 23000  # м/с
alpha = -pi / 3  # угол между вектором скорости и x
x_0 = 0  # м
y_0 = 5  # м
m = 0.001  # кг
q = 0.001  # Кл
Q = 0.07  # Кл
eps_0 = 8.85 * 10 ** (-12)
k = 1 / (4 * pi * eps_0)  # коэффициент


# ---- параметры для моделирования ---- #
dt = 0.000001  # с
T_array = [0]  # список, хранящий время
X_array = [x_0]  # список, хранящий итерации по x
Y_array = [y_0]  # список, хранящий итерации по y
Vx_array = [v_0 * cos(alpha)]  # список, хранящий итерации проекции скорости по x
Vy_array = [v_0 * sin(alpha)]  # список, хранящий итерации проекции скорости по y


# ---- функция, отсчитывающая время ---- #
def t_counter(t):
    return t + dt


# ---- функция, отсчитывающая x ---- #
def x_counter(x, x_first):
    a = x + dt * x_first
    return a


# ---- функция, отсчитывающая y ---- #
def y_counter(y, y_first):
    a = y + dt * y_first
    return a


# ---- функция, отсчитывающая x' ---- #
def x_frst(x_first, x_second):
    a = x_first + dt * x_second
    return a


# ---- функция, отсчитывающая y' ---- #
def y_frst(y_first, y_second):
    a = y_first + dt * y_second
    return a


# ---- функция, отсчитывающая x'' ---- #
def x_scnd(x, y):
    a = (k * q * Q / m) * x * ((x ** 2 + y ** 2) ** (-3 / 2))
    return a


# ---- функция, отсчитывающая y'' ---- #
def y_scnd(x, y):
    a = (k * q * Q / m) * y * ((x ** 2 + y ** 2) ** (-3 / 2))
    return a


# ---- основная функция подсчета ---- #
def constructor():
    for i in range(30000):
        T_array.append(t_counter(T_array[-1]))
        Vx_array.append(x_frst(Vx_array[-1], x_scnd(X_array[-1], Y_array[-1])))
        Vy_array.append(y_frst(Vy_array[-1], y_scnd(X_array[-1], Y_array[-1])))
        X_array.append(x_counter(X_array[-1], Vx_array[-1]))
        Y_array.append(y_counter(Y_array[-1], Vy_array[-1]))

    return X_array, Y_array


Tuple = constructor()


# ---- строим график ----#

plt.xlabel('x, м', fontsize=16)
plt.ylabel('y, м', fontsize=16)
plt.title('Траектория движения частицы q')
plt.plot(Tuple[0], Tuple[1])

plt.grid(which='major')
# ---- включаем дополнительную сетку ---- #
plt.grid(which='minor', linestyle=':')
plt.tight_layout()
center_Q = 0.0, 0.0
c_Q = plt.Circle(center_Q, radius=0.3, color="m")
plt.gca().add_artist(c_Q)
center_q_st = x_0, y_0
c_q_start = plt.Circle(center_q_st, radius=0.1, color="k")
plt.gca().add_artist(c_q_start)
plt.xlim(-8, 8)
plt.ylim(-6, 6)
plt.show()

