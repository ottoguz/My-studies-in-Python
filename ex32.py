from datetime import date
year = int(input('Which year would you like to analyze? Put "0" to analyze the current year.'))
if year == 0:
    year = date.today().year
if (year % 4 == 0) and (year % 100 != 0) or (year % 400 == 0):
    print('The year {} is a LEAP YEAR'.format(year))
else:
    print('The year {} is NOT a LEAP YEAR'.format(year))

