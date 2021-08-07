#Create a program which reads the int portion of any real number
import math
rnum = float(input('Type a real value:'))
int = math.trunc(rnum)
print('The value typed was: {} and its integral proportion is: {}.'.format(rnum, int))


