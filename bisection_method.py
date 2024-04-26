def bisection_method(func, a, b, tol=1e-6, max_iter=100):
    if func(a) * func(b) >= 0:
        print("Bisection method fails.")
        return None

    for _ in range(max_iter):
        c = (a + b) / 2
        if func(c) == 0 or (b - a) / 2 < tol:
            return c
        if func(c) * func(a) < 0:
            b = c
        else:
            a = c
    return None

# Example usage:
if __name__ == "__main__":
    def f(x):
        return x**3 - 2*x - 5

    a = 1
    b = 3

    root = bisection_method(f, a, b)
    if root is not None:
        print("Approximate root:", root)
    else:
        print("No root found within the maximum number of iterations.")