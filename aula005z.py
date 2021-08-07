i = 0
while True:
    try:
        name = input('Type in a name:')
        ind = int(input('Type in  an index:'))
        print(name[ind])
    except ValueError:
        print('Ooops, invalid name! Try again!')
    except IndexError:
        print('Ooops, invalid index!')
    finally:
        print('Attempt #{}.' .format(i))
        i += 1



