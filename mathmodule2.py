import math

def angle_demo():
    angle = math.sin(math.pi/2) # default input is in radians
    print(angle)
    
    # Converting degrees to radians first
    angle = math.sin(math.radians(90))
    print(angle)

angle_demo()

