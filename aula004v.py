#CALCULATOR (WITH REPETITION CILCES)
print('CALCULATOR')
print('+ SUM')
print('- SUBTRACTION')
print('x MULTIPLICATION')
print(': DIVISION')
print('Press "s" to leave')

while True:
    op = input('Choose an operation:')
    if (op == '+') or (op == '-') or (op == 'x') or (op == ':'):
        v1 = int(input('Value 1:'))
        v2 = int(input('Value 2:'))

    if (op == '+'):
        res = v1 + v2
        print('{} + {} = {}' .format(v1, v2, res))
        continue
    elif (op == '-'):
        res = v1 - v2
        print('{} - {} = {}' .format(v1, v2, res))
        continue
    elif (op == 'x'):
        res = v1 * v2
        print('{} x {} = {}' .format(v1, v2, res))
        continue
    elif (op == ':'):
        res = v1 / v2
        print('{} : {} = {}' .format(v1, v2, res))
        continue
    elif (op == 's'):
        print('Closing the program...')
        break
    else:
        print('Inválaid operation!')




