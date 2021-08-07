#CALCULATOR
calc = 'CALCULATOR'
print('{:=^20}' .format(calc))

print('+ SOM')
print('- SUBTRACTION')
print('x MULTIPLICATION')
print(': DIVISION')

op = input('Choose an operation:')
v1 = int(input('Value 1:'))
v2 = int(input('Value 2:'))

if op == '+':
    print('{} + {} = {}' .format (v1, v2, v1 + v2))
elif op == '-':
    print('{} - {} = {}' .format(v1, v2, v1 - v2))
elif op == 'x':
    print('{} x {} = {}' .format(v1, v2, v1 * v2))
elif op == ':':
    print('{} : {} = {}' .format(v1, v2, v1 / v2))
else:
    print('Inexistent operation!')
print('Closing the program...')

















