from random import choice
n1 = str(input('1st Student:'))
n2 = str(input('2nd Student:'))
n3 = str(input('3rd Student:'))
n4 = str(input('4th Student:'))
list = [n1, n2, n3, n4]
chosen = choice(list)
print('The chosen student was{}.' .format(chosen))

