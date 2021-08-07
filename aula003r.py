# Triangles
A = int(input('Angle 1:'))
B = int(input('Angle 2:'))
C = int(input('Angle 3:'))

#Conditionals to verify the minimum requirements to form a triangle
if (A > 0) and (B > 0) and (C > 0):
    if (A + B > C) and (A + C > B) and (B + C > A):
#This section verifies the type o triangle
        if (A != B) and (B != C) and (C != A):
            print('Scalene triangle!')
        elif (A == B) and (B == C) and (C == A):
            print('Equilateral triangle!')
        else:
            print('Isoceles triangle!')
    else:
        print('These values will not form a triangle')
else:
    print('These values will not form a triangle')















