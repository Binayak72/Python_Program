# Implementation of Roots Finding Methods (Newton Raphson Method, Bisection Method) in python.

def newton_raphson(func, func_derivative, initial_guess, tol=1e-6, max_iter=100):
    x = initial_guess
    for _ in range(max_iter):
        x_new = x - func(x) / func_derivative(x)
        if abs(x_new - x) < tol:
            return x_new
        x = x_new
    return None

if __name__ == "__main__":
    def f(x):
        return x**3 - 2*x - 5

    def f_prime(x):
        return 3*x**2 - 2

    initial_guess = 2

    root = newton_raphson(f, f_prime, initial_guess)
    if root is not None:
        print("Approximate root of function f(x)=x**3-2*x-5 ::", root)
    else:
        print("No root found within the maximum number of iterations.")
