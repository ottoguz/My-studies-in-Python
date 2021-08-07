#daily rate = R$60 e km = R$0.15 calculate the price
km = float(input('Type in the distance driven:'))
daily_rate = int(input('Type in the days driven:'))
total = (km * 0.15) + (daily_rate * 60)
print('Milage: {}Km. Days: {}. Total to be paid: R${}.' .format(km, daily_rate, total))
