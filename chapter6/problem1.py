from math import sin, cos, pi

def calculation(n):
    #PI = 3.141592
    m = n*pi/180
    return sin(m)+cos(m)

Angle = float(input("Input Angle : "))
print(calculation(Angle))
    

