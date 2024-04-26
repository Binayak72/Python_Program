import math

def simpson_1_3(f, a, b, n):

  h = (b - a) / n
  sum = f(a) + f(b)
  for i in range(2, n, 2):
    sum += 4 * f(a + i * h)
  for i in range(3, n - 1, 2):
    sum += 2 * f(a + i * h)
  return sum * h / 3


def f(x):
  return math.sin(x)

a = 0
b = math.pi
n = 100

integral = simpson_1_3(f, a, b, n)

print("The numerical integral of f(x) = sin(x) over [0, pi] is:", integral)