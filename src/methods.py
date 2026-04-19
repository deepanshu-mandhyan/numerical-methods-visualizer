def bisection(f, a, b, tol):
    errors = []
    c_old = a
    iterations = 0

    if f(a) * f(b) >= 0:
        return None, None, None

    while (b - a) > tol:
        c = (a + b) / 2
        error = abs(c - c_old)
        errors.append(error)

        if f(c) == 0:
            break
        elif f(a) * f(c) < 0:
            b = c
        else:
            a = c

        c_old = c
        iterations += 1

    return c, errors, iterations


def newton(f, df, x0, tol):
    errors = []
    x = x0
    iterations = 0

    while True:
        if df(x) == 0:
            return None, None, None

        x_new = x - f(x) / df(x)
        error = abs(x_new - x)
        errors.append(error)

        if error < tol:
            break

        x = x_new
        iterations += 1

    return x_new, errors, iterations
