#A program whihc shows the length of the hypotenuse
# c1² + c2² = h²
import math
c1 = float(input('Cathetus 1:'))
c2 = float(input('Cathetus 2:'))
c1_pow_c2_pow = math.pow(c1, 2) + math.pow(c2, 2)
hip = math.sqrt(c1_pow_c2_pow)
print('This triangle hypotenuse is: {}' .format(hip))







