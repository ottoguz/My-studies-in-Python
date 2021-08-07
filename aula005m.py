while True:
    try:
        x = int(input('Type an integer:'))
        break
    except ValueError:
        print('Oops, invalid value!')
