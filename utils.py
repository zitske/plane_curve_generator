from math import tan, radians
def calculate_radius(v,a):
    #Formula: R=(Vˆ2)/11.26*tg(30)
    #v= v/1.852; #Uncoment to use km/h instead of knots on input
    angle_in_radians = radians(a)
    result = (v**2)/(11.26*tan(angle_in_radians));
    result = result*0.3048; #Convert to meters
    return result;