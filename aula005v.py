def great3(v1 = 0, v2 = 0, v3 = 0):
    if v1 and v2 and v3:
        if (v1 > v2) and (v1 > v3):
            if v2 > v3:
                print('increasing order: {}, {}, {}.' .format(v3, v2, v1, end=' '))
            else:
                print('Increasing order: {}, {}, {}.' .format(v2, v3, v1, end=''))
        elif (v2 > v1) and (v2 > v3):
            if v1 > v3:
                print('Increasing order: {}, {}, {}.' .format(v3, v1, v2, end=''))
            else:
                print('Increasing order: {}. {}, {}.' .format(v1, v3, v2, end=''))
        elif(v3 > v1) and (v3 > v2):
            if v1 > v2:
                print('Increasing order: {}, {}, {}.' .format(v2, v1, v3, end=''))
            else:
                print('Increasing order: {}, {}, {}.' .format(v1, v2, v3, end=''))


#main program


x = int(input('Type a value for x:'))
y = int(input('Type a value for y:'))
z = int(input('Type a value for z:'))

great3(x, y, z)






