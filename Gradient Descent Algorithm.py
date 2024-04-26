def gradient_descent(learning_rate, epochs):
    theta = 0
    data = [2, 4, 6, 8]
    m = len(data)

    for _ in range(epochs):
        gradient = 0
        for i in range(m):
            gradient += (theta * data[i] - 10) * data[i]
        theta = theta - (learning_rate * gradient)

    return theta


learning_rate = 0.01
epochs = 1000
result = gradient_descent(learning_rate, epochs)
print("Optimized value:", result)
