
import numpy as np
import matplotlib.pyplot as plt

from utils import calculate_radius
from collections import namedtuple

point = namedtuple('point', ['longitude', 'latitude', 'altitude', 'velocity'])


v = 120; # Aircraft speed in knots
a = 30; # Curver angle in degrees


# Example usage
aircraft_state = point(longitude=34.0522, latitude=-118.2437, altitude=10000, velocity=120)

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