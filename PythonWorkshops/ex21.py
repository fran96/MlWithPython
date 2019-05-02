def add(a, b):
    answer = a + b
    print(f"ADDING {a} + {b}")
    return answer

def subtract(a, b):
    answer = a - b
    print(f"SUBTRACTING {a} - {b}")
    return answer

def multiply(a, b):
    answer = a * b
    print(f"MULTIPLYING {a} * {b}")
    return answer

def divide(a, b):
    answer = a / b
    print(f"DIVIDING {a} / {b}")
    return answer

print("Lets do some math with just functions")

age = add(30, 5)
height = subtract(78, 4)
weight = multiply(90, 2)
iq = divide(100, 2)

print(f"Age: {age}, Height: {height}, Weight: {weight}, IQ: {iq}")

print("Here is a puzzle")

what = add(age, subtract(height, multiply(weight, divide(iq, 2))))
