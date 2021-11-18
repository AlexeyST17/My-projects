import random
import matplotlib.pyplot as plt
import numpy as np

sigma = 5.669e-8
eps = 1e-5

number_of_knots_x = int(input("Input number of knots x (N_x) : "))
number_of_knots_y = int(input("Input number of knots x (N_x) : "))
number_x = int(number_of_knots_x / 2)
number_y = int(number_of_knots_y / 2)

print(number_x, number_y)

time_finish = float(input("Input your finish time (t_end): "))
thickness_of_plate_x = 0.25  # float(input("Thickness of plate (L_x): "))
thickness_of_plate_y = 0.31  # float(input("Thickness of plate (L_y): "))
lambda_of_plate = 46  # float(input("Thermal conductivity (lambda): "))
density_of_plate = 7800  # float(input("Density of plate (ro): "))
heat_capacity_of_plate = 460  # float(input("Heat capacity of plate (c): "))
kappa1_at_x0_y0_0 = float(input("kappa1"))
kappa2_at_x0_y0_HL = float(input("kappa2"))
start_temperature = 30  # float(input("Start temperature of plate (T0): "))
Te1 = float(input("temp of sreda x = 0, y = 0"))
Te2 = float(input("Temp of sreda x = L, y = H"))
eps1 = float(input("Blackness"))

# def select_direction(number_of_x, number_of_y):
#     abc = random.random()
#     if 0 <= abc < 0.25 and number_of_y - 1 >= 0:
#         T[number_of_x][number_of_y - 1] = T[number_of_x][number_of_y]
#         T[number_of_x][number_of_y] = start_temperature
#         number_of_y -= 1
#         return number_of_x, number_of_y
#     elif 0.25 <= abc < 0.5 and number_of_x - 1 >= 0:
#         T[number_of_x - 1][number_of_y] = T[number_of_x][number_of_y]
#         T[number_of_x][number_of_y] = start_temperature
#         number_of_x -= 1
#         return number_of_x, number_of_y
#     elif 0.5 <= abc < 0.75 and number_of_y + 1 <= number_of_knots_y-1:
#         T[number_of_x][number_of_y + 1] = T[number_of_x][number_of_y]
#         T[number_of_x][number_of_y] = start_temperature
#         number_of_y += 1
#         return number_of_x, number_of_y
#     elif 0.75 <= abc < 1.0 and number_of_x + 1 <= number_of_knots_x-1:
#         T[number_of_x + 1][number_of_y] = T[number_of_x][number_of_y]
#         T[number_of_x][number_of_y] = start_temperature
#         number_of_x += 1
#         return number_of_x, number_of_y


# temperature_at_x0 = 400  # float(input("Start temperature of plate at x = 0 (Tl): "))
# temperature_at_xl = 100  # float(input("Start temperature of plate at x = L (Tr): "))
# temperature_at_xleft = 150  # float(input("Start temperature of plate at x = 0 (Tl): "))
# temperature_at_xright = 3200  # float(input("Start temperature of plate at x = L (Tr): "))

T = [[0.0 for i in range(number_of_knots_y)] for j in range(number_of_knots_x)]
Tn = [[0.0 for i in range(number_of_knots_y)] for j in range(number_of_knots_x)]

h_x = thickness_of_plate_x / (number_of_knots_x - 1)
h_y = thickness_of_plate_y / (number_of_knots_y - 1)
tau = time_finish / 1000
time = 0.0
for i in range(number_of_knots_x):
    for j in range(number_of_knots_y):
        T[i][j] = start_temperature

alfa = [0.0 for i in range(max(number_of_knots_y, number_of_knots_x))]
beta = [0.0 for i in range(max(number_of_knots_y, number_of_knots_x))]

fig, ax = plt.subplots(figsize=(6, 6))

X = np.linspace(0, thickness_of_plate_x, num=number_of_knots_x)
Y = np.linspace(0, thickness_of_plate_y, num=number_of_knots_y)

Xmesh, Ymesh = np.meshgrid(X, Y)

while True:
    if time >= time_finish:
        break
    # print("TIME NOW: ", time)
    time += tau

    for i in range(number_of_knots_x):
        for j in range(number_of_knots_y):
            Tn[i][j] = T[i][j]

    cd = 0
    ef = 0
    abc = random.random()
    if 0 <= abc < 0.25 and number_y - 1 >= 0:
        tmp = T[number_x][number_y - 1]
        T[number_x][number_y - 1] = 50
        T[number_x][number_y] = tmp
        number_y -= 1
        cd += number_x
        ef += number_y
    elif 0.25 <= abc < 0.5 and number_x - 1 >= 0:
        tmp = T[number_x - 1][number_y]
        T[number_x - 1][number_y] = 50
        T[number_x][number_y] = tmp
        number_x -= 1
        cd += number_x
        ef += number_y
    elif 0.5 <= abc < 0.75 and number_y + 1 <= number_of_knots_y - 1:
        tmp = T[number_x][number_y + 1]
        T[number_x][number_y + 1] = 50
        T[number_x][number_y] = tmp
        number_y += 1
        cd += number_x
        ef += number_y
    elif 0.75 <= abc < 1.0 and number_x + 1 <= number_of_knots_x - 1:
        tmp = T[number_x + 1][number_y]
        T[number_x + 1][number_y] = 50
        T[number_x][number_y] = tmp
        number_x += 1
        cd += number_x
        ef += number_y

    for j in range(number_of_knots_y):
        alfa[0] = 2.0 * tau * lambda_of_plate / (2.0 * tau * (lambda_of_plate + kappa1_at_x0_y0_0 * h_x) +
                                                 density_of_plate * heat_capacity_of_plate * (h_x ** 2))
        while True:
            d = T[0][j - 1]
            beta[0] = (density_of_plate * heat_capacity_of_plate * (h_x ** 2) * Tn[0][
                j - 1] + 2.0 * tau * kappa1_at_x0_y0_0 * h_x * Te1 +
                       2.0 * tau * eps1 * sigma * h_x * (Te1 ** 4 - d ** 4)) / (
                              2.0 * tau * (lambda_of_plate + kappa1_at_x0_y0_0 * h_x)
                              + density_of_plate * heat_capacity_of_plate * (h_x ** 2))

            for i in range(1, number_of_knots_x - 1):
                ai = lambda_of_plate / (h_x ** 2)
                bi = 2.0 * lambda_of_plate / (h_x ** 2) + density_of_plate * heat_capacity_of_plate / tau
                ci = lambda_of_plate / (h_x ** 2)
                fi = -density_of_plate * heat_capacity_of_plate * Tn[i][j] / tau
                alfa[i] = ai / (bi - ci * alfa[i - 1])
                beta[i] = (ci * beta[i - 1] - fi) / (bi - ci * alfa[i - 1])
            T[number_of_knots_x - 1][j] = (density_of_plate * heat_capacity_of_plate * (h_x ** 2) *
                                           Tn[number_of_knots_x - 1][j] +
                                           2.0 * tau * lambda_of_plate * beta[number_of_knots_x - 2]) \
                                          / (density_of_plate * heat_capacity_of_plate * h_x ** 2 + 2.0 * tau *
                                             lambda_of_plate * (1 - alfa[number_of_knots_x - 2]))

            for i in range(number_of_knots_x - 2, -1, -1):
                T[i][j] = alfa[i] * T[i + 1][j] + beta[i]
            if np.abs(d - T[0][j - 1]) <= eps:
                break
    T[cd][ef] = 50
    for i in range(number_of_knots_x - 1):
        alfa[0] = 2.0 * lambda_of_plate * tau / \
                  (2.0 * tau * lambda_of_plate + density_of_plate * heat_capacity_of_plate * (h_y ** 2))
        beta[0] = (h_y ** 2) * density_of_plate * heat_capacity_of_plate * T[i][0] / \
                  (2.0 * tau * lambda_of_plate + density_of_plate * heat_capacity_of_plate * (h_y ** 2))
        for j in range(1, number_of_knots_y - 1):
            ai = lambda_of_plate / (h_y ** 2)
            bi = 2.0 * lambda_of_plate / (h_y ** 2) + density_of_plate * heat_capacity_of_plate / tau
            ci = lambda_of_plate / (h_y ** 2)
            fi = -density_of_plate * heat_capacity_of_plate * T[i][j] / tau
            alfa[j] = ai / (bi - ci * alfa[j - 1])
            beta[j] = (ci * beta[j - 1] - fi) / (bi - ci * alfa[j - 1])
        d = T[i][number_of_knots_y - 1]
        while True:
            d1 = T[i][number_of_knots_y - 1]
            T[i][number_of_knots_y - 1] = (density_of_plate * heat_capacity_of_plate * h_y ** 2 * d +
                                           2.0 * tau * (lambda_of_plate * beta[number_of_knots_y - 2] +
                                                        kappa2_at_x0_y0_HL * h_y * Te2 +
                                                        eps1 * sigma * h_y * (Te2 ** 4 - d1 ** 4))) / \
                                          (density_of_plate * heat_capacity_of_plate * h_y ** 2 + 2.0 * tau * (
                                                  lambda_of_plate * (
                                                  1 - alfa[number_of_knots_y - 2] + kappa2_at_x0_y0_HL * h_y
                                          )))
            if np.abs(d1 - T[i][number_of_knots_y - 1]) <= eps:
                break
            for j in range(number_of_knots_y - 2, -1, -1):
                T[i][j] = alfa[j] * T[i][j + 1] + beta[j]
    cd = 0
    ef = 0
    plt.pcolormesh(Y, X, T)
    # plt.colorbar()
    plt.draw()
    plt.pause(0.005)
    # if time < time_finish:
    #     plt.close()

plt.close()
plt.pcolormesh(Y, X, T)
plt.colorbar()
plt.show()

for i in T:
    for j in i:
        print(j, end=", ")
    print()
