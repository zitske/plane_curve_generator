from math import tan, radians
import numpy as np
import matplotlib.pyplot as plt
#(Vˆ2)/11.26*tg(30)

v = 120; # Aircraft speed in knots
a = 30; # Curver angle in degrees

def calculate_radius(v,a):
    #v= v/1.852; #Uncoment to use km/h instead of knots on input
    angle_in_radians = radians(a)
    result = (v**2)/(11.26*tan(angle_in_radians));
    result = result*0.3048; #Convert to meters
    return result;


radius = calculate_radius(v, a)

theta = np.linspace(0, 2 * np.pi, 100)
x = radius * np.cos(theta)
y = radius * np.sin(theta)

plt.plot(x, y)
plt.gca().set_aspect('equal', adjustable='box')
plt.title(f'Curve with radius: {radius:.2f} meters')
plt.xlabel('x (meters)')
plt.ylabel('y (meters)')
plt.grid(True)
plt.show()