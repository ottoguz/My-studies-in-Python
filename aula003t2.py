#EXERCÍCIO 3
type_inst = input('What type of electricity grid?\n(R - Residential)\n(C- Commercial)\n(I - Industrial)\nTYPE IN:')
consumption = float(input('What was your consumption(Kw/h)?\nTYPE IN:'))

if type_inst == 'R'.lower():
    if consumption <= 500:
        total = consumption * 0.4
    elif consumption > 500:
        total = consumption * 0.6
elif type_inst == 'C'.lower():
    if consumption <= 500:
        total = consumption * 0.55
    elif consumption > 500:
        total = consumption * 0.6
elif type_inst == 'I'.lower():
    if consumption <= 500:
        total = consumption * 0.55
    elif consumption > 500:
        total = consumption* 0.6
else:
    print('Inexistent grid!')
print('Total to be charged: R$ {:.2f}' .format(total))
















