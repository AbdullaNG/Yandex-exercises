def roots_of_quadratic_equation(a, b, c):
    if a == 0 and b == 0 and c == 0:
        return ['all']
    elif a == 0 and b == 0:
        return []
    elif c == 0:
        return [0, -b / a]
    elif a == 0:
        return [-c / b]
    else:
        d = b ** 2 - 4 * a * c
        if d > 0:
            x1 = ((-b + d ** 0.5) / (2 * a))
            x2 = ((-b - d ** 0.5) / (2 * a))
            return[x1, x2]
        elif d == 0:
            return [-b / (2 * a)]
        else:
            return []