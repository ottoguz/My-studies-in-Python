#Faça um programa que faça a leitura do cateto oposto e do cateto adjacente de um triangula retângulo, calcule e mostre o comprimento da hipotenusa
# c1² + c2² = h²
from math import pow, sqrt
c1 = float(input('Cathetus 1:'))
c2 = float(input('Cathetus 2:'))
c1_pow_c2_pow = pow(c1, 2) + pow(c2, 2)
hip = sqrt(c1_pow_c2_pow)
print('This triangle hypotenuse is: {}' .format(hip))

