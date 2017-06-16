from math import sqrt


def get_roots(a, b, c):
    #найти дискриминант
    discriminant = b ** 2 - 4 * a * c
    #исходя из значения дискриминанта найти корни
    if discriminant == 0:
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        return root1, None
    elif discriminant > 0:
        root1 = (-b - sqrt(discriminant)) / (2 * a)
        root2 = (-b + sqrt(discriminant)) / (2 * a)
        return root1, root2
    else:
        return None, None
