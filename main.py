import math

def target_function(x):
    return 2*x**2 - 8*x + 12

def first_derivative(x):
    return 4*x - 8

def second_derivative():
    return 4

# Метод бісекції
def bisection_min(df, a, b, precision=0.001):
    count_of_iteration = 0
    while (b - a)/2 > precision:
        c = (a + b) / 2
        if df(c) == 0:
            return c, count_of_iteration
        elif df(a) * df(c) < 0:
            b = c
        else:
            a = c
        count_of_iteration += 1
    return (a + b) / 2, count_of_iteration

# Метод золотого перетину
def golden_section_min(f, a, b, precision=0.001):
    count_of_iteration = 0
    golder_ratio = (math.sqrt(5) + 1) / 2

    c = b - (b - a) / golder_ratio
    d = a + (b - a) / golder_ratio

    while abs(b - a) > precision:
        if f(c) < f(d):
            b = d
        else:
            a = c

        c = b - (b - a) / golder_ratio
        d = a + (b - a) / golder_ratio
        count_of_iteration += 1

    return (a + b) / 2, count_of_iteration

# Метод дотичних
def derivative_min(first_derivative, second_derivative, start_point_x0=3.0, precision=0.001, max_iteration=100):
    count_of_iteration = 0
    while count_of_iteration < max_iteration:
        x1 = start_point_x0 - first_derivative(start_point_x0) / second_derivative()
        if abs(first_derivative(x1)) < precision:
            return x1, count_of_iteration
        start_point_x0 = x1
        count_of_iteration += 1
    return start_point_x0, count_of_iteration

a = 1.0
b = 5.9

min_bisect, count_of_iteration_bisect = bisection_min(first_derivative, a, b)
min_golden, count_of_iteration_golden = golden_section_min(target_function, a, b)
min_newton, iteration_of_derivative = derivative_min(first_derivative, second_derivative, start_point_x0=3.0)

print(f"Метод бісекції:  Мінімум x = {min_bisect}, ітерацій: {count_of_iteration_bisect}")
print(f"Метод золотого перетину: Мінімум x = {min_golden}, ітерацій: {count_of_iteration_golden}")
print(f"Метод дотичних:  Мінімум x = {min_newton}, ітерацій: {iteration_of_derivative}")