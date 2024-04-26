def secant_method(func, x0, x1, tol=1e-6, max_iter=100):
    for i in range(max_iter):
        x2 = x1 - func(x1) * (x1 - x0) / (func(x1) - func(x0))
        if abs(x2 - x1) < tol:
            return x2
        x0 = x1
        x1 = x2
    return None

if __name__ == "__main__":
    def f(x):
        return x**3 - 2*x - 5

    x0 = 1
    x1 = 3

    root = secant_method(f, x0, x1)
    if root is not None:
        print("Approximate root:", root)
    else:
        print("No root found within the maximum number of iterations.")
