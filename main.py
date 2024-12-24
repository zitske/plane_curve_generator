from math import tan, radians

#(Vˆ2)/11.26*tg(30)

v = 120; #km/h


def calculate(v):
    v= v/1.852; #knots
    angle_in_radians = radians(30)
    return (v**2)/(11.26*tan(angle_in_radians))

print(calculate(v));