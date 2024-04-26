def f(x):
    return x**3 - 2*x - 5

def f_prime(x):
    return 3*x**2 - 2

def newton_raphson_forward(func, func_prime, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        x_new = x - func(x) / func_prime(x)
        if abs(x_new - x) < tol:
            return x_new, i + 1
        x = x_new
    return None, max_iter

def newton_raphson_backward(func, func_prime, x0, tol=1e-6, max_iter=100):
    x = x0
    for i in range(max_iter):
        x_new = x + func(x) / func_prime(x)
        if abs(x_new - x) < tol:
            return x_new, i + 1
        x = x_new
    return None, max_iter

x0 = 2
root_forward, iterations_forward = newton_raphson_forward(f, f_prime, x0)
root_backward, iterations_backward = newton_raphson_backward(f, f_prime, x0)

print("Root (forward method):", root_forward)
print("Number of iterations (forward method):", iterations_forward)
print("Root (backward method):", root_backward)
print("Number of iterations (backward method):", iterations_backward)

