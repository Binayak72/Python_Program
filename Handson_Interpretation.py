from scipy.optimize import newton

# Define the function
def f(x):
    return x**3 - 2*x - 5

# Define the derivative of the function
def f_prime(x):
    return 3*x**2 - 2

# Initial guess
x0 = 2

# Use the newton function to find the root
root = newton(f, x0, fprime=f_prime)

print("Root found using Newton-Raphson method:", root)
