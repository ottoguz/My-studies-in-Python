#AULA PRÁTICA 4 EXER 3

total = 0
revenue = 0

while True:
    age = input('Age:')
    if (age == 'leave'):
        break
    age = int(age)
    total += 1
    if (age < 3):
        ticket = 0
    elif (age > 12):
        ticket = 30
    else:
        ticket = 15
    revenue += ticket
average = revenue / total
print('Average paid per ticket: R$ {:.2f}' .format(average))
print('Total of people: {}' .format(total))
print('Total revenue: R$ {:.2f}' .format(revenue))
