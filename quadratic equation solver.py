import math

def quadratic_file_solver(a, b, c):
    
    d = b**2 - (4 * a * c)
    
    if d < 0:
        result = "Complex Roots (No real solution)"
    else:
        # Standard Quadratic Formula
        x1 = (-b + math.sqrt(d)) / (2 * a)
        x2 = (-b - math.sqrt(d)) / (2 * a)
        result = f"x1 = {x1}, x2 = {x2}"
    
  
    file = open("quadratic_results.txt", "a")
    file.write(f"Equation: {a}x^2 + {b}x + {c} = 0 | Result: {result}\n")
    file.close()
    
    return result


print(quadratic_file_solver(3, -10, 7))