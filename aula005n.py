def division():
    try:
        v1 = int(input('Value 1:'))
        v2 = int(input('Value 2:'))
        res = v1 / v2

    except ZeroDivisionError:
        print('Cannot divide a number by zero!')

    except:
        print('Ooops, something went wrong!')

    else:
        print(res)

    finally:
        print('Will always execute...')


division()
