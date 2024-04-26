import numpy as np
def hardness(cooling_rate):
    return -0.1 * cooling_rate ** 2 + 5 * cooling_rate + 50

def scent_method(initial_guess, step_size, tolerance, max_iterations):
    current_guess = initial_guess
    iteration = 0

    while iteration < max_iterations:
        current_hardness = hardness(current_guess)

        next_guess = current_guess + step_size * np.random.uniform(-1, 1)
        next_hardness = hardness(next_guess)

        if abs(next_hardness - current_hardness) < tolerance:
            return next_guess

        current_guess = next_guess
        iteration += 1

    return current_guess


initial_guess = 10.0
step_size = 0.1
tolerance = 0.01
max_iterations = 1000

optimal_cooling_rate = scent_method(initial_guess, step_size, tolerance, max_iterations)
optimal_hardness = hardness(optimal_cooling_rate)

print(f"Optimal Cooling Rate: {optimal_cooling_rate}")
print(f"Optimal Hardness: {optimal_hardness}")