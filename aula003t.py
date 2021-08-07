#ELECTRICITY BILL
type_inst = input('What type of electricity grid?\n(R - Residential)\n(C- Commercial)\n(I - Industrial)\nTYPE IN:')
consumption = float(input('What was your consumption(Kw/h)?\nTYPE IN:'))


if type_inst == 'R'.lower():
    if consumption <= 500:
        total = consumption * 0.4
        print('Total to be charged: R$ {:.2f}' .format(total))
    elif consumption > 500:
        total = consumption * 0.6
        print('Total to be charged: R$ {:.2f}' .format(total))
elif type_inst == 'C'.lower():
    if consumption <= 500:
        total = consumption * 0.55
        print('Total to be charged: R$ {:.2f}' .format(total))
    elif consumption > 500:
        total = consumption * 0.6
        print('Total to be charged: R$ {:.2f}' .format(total))
elif type_inst == 'I'.lower():
    if consumption <= 500:
        total = consumption * 0.55
        print('Total to be charged: R$ {:.2f}' .format(total))
    elif consumption > 500:
        total = consumption * 0.6
        print('Total to be charged: R$ {:.2f}' .format(total))
else:
    print('Inexistent grid!')
print('Closing the program...')













