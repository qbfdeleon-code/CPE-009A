import math

def projectilemotion_solver(velocity, angle_degrees):
    
    g = 9.8
    
    theta = math.radians(angle_degrees)
    
    horizontalRange = (velocity**2 * math.sin(2 * theta)) / g
    
    max_height = (velocity**2 * (math.sin(theta)**2)) / (2 * g)
    
    return horizontalRange, max_height


v = 11.0
angle = 20.0

dist, height = projectilemotion_solver(v, angle)

print(f"Horizontal Distance (Range): {dist:.2f} m")
print(f"Maximum Height: {height:.2f} m")