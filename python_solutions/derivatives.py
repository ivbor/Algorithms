import random
import math

def deriv(func, curr_x, eps = 1e-6):
    return ((func(curr_x + eps) - func(curr_x))/eps)

def extrema(func, start, end, eps = 1e-6):
    extrema_list = []
    curr_x = start
    curr_deriv = deriv(func, curr_x, eps)
    while (curr_x + eps <= end):
        ex_deriv = curr_deriv
        curr_deriv = deriv(func, curr_x, eps)
        if (abs(ex_deriv) <= eps and abs(curr_deriv) > eps):
            extrema_list.append((curr_x-eps, func(curr_x-eps)))
        curr_x += eps
    if (len(extrema_list) == 0 or len(extrema_list) == 1):
        extrema_list.append((start, func(start)))
        extrema_list.append((end, func(end)))
    return extrema_list

def integral(func = math.sin, eps = 1e-6, start = 0, end = math.pi, der_eps = 0):
    if der_eps == 0:
        extrema_list = extrema(func, start, end)
    else:
        extrema_list = extrema(func, start, end, eps = der_eps)
    extrema_y_list = [i[1] for i in extrema_list]
    delta = eps / (max(extrema_y_list) - min(extrema_y_list))
    num_dx = int((end - start) / delta)
    integr = 0
    curr_x = start
    for i in range(num_dx+1):
        curr_x = start + i*delta + random.uniform(0, delta)
        integr += delta * func(curr_x)
    return integr
