from math import sin, cos, tan, radians
ang = float(input('Type an angle:'))
# Used the function math.radians() to turn numbers into radians
print('Sine {:.2f}:' .format(sin(radians(ang))))
print('Cosene {:.2f}:'.format(cos(radians(ang))))
print('Tangent {:.2f}:' .format(tan(radians(ang))))
