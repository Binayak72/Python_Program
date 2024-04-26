from scipy.optimize import minimize


def objective_function(x):
    return x[0] ** 2 + x[1] ** 2


def constraint_equation(x):
    return x[0] + x[1] - 1


def lagrange_multiplier(x):
    lambda_ = x[-1]
    return objective_function(x[:-1]) + lambda_ * constraint_equation(x[:-1])


x0 = [0, 0, 0]

solution = minimize(lagrange_multiplier, x0, method='SLSQP', constraints={'type': 'eq', 'fun': constraint_equation})

print("Optimal Solution:", solution.x[:-1])
print("Optimal Lambda:", solution.x[-1])
print("Objective Value at Optimal Solution:", objective_function(solution.x[:-1]))

