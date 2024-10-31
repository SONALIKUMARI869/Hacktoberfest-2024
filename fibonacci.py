import math

def fibonacci_formula(n):
    phi = (1 + math.sqrt(5)) / 2
    return round((phi ** n - (-1 / phi) ** n) / math.sqrt(5))

print(fibonacci_formula(10))  # Output: 55
