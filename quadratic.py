import math

def solve_quadratic(a, b, c):
    # Calculate the discriminant
    discriminant = b**2 - 4*a*c

    # Check if the discriminant is positive, zero or negative
    if discriminant > 0:
        # Two real and distinct roots
        root1 = (-b + math.sqrt(discriminant)) / (2 * a)
        root2 = (-b - math.sqrt(discriminant)) / (2 * a)
        return f"Two distinct real roots: {root1} and {root2}"
    elif discriminant == 0:
        # One real root (repeated)
        root = -b / (2 * a)
        return f"One real repeated root: {root}"
    else:
        # Complex roots
        real_part = -b / (2 * a)
        imaginary_part = math.sqrt(-discriminant) / (2 * a)
        return f"Two complex roots: {real_part} + {imaginary_part}i and {real_part} - {imaginary_part}i"

# Input coefficients from the user
a = float(input("Enter coefficient a: "))
b = float(input("Enter coefficient b: "))
c = float(input("Enter coefficient c: "))

# Check if it's a valid quadratic equation
if a == 0:
    print("Coefficient 'a' cannot be zero for a quadratic equation.")
else:
    # Solve the quadratic equation
    result = solve_quadratic(a, b, c)
    print(result)
