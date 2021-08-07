#DOLLAR BILLS COUNT

value = int(input('Type the desired value(R$):'))

while True:
    #verifies if there are USD 100 bills
    if (value  >= 100):
        bills100 = value // 100
        value  -= bills100 * 100
        print('USD 100 bills: {}' .format(bills100))
        if not value:
            break


    # verifies if there are USD 50 bills
    if (value >= 50):
        bills50 = value // 50
        value -= bills50 * 50
        print('USD 50 bills: {}' .format(bills50))
        if not value:
            break


    # verifies if there are USD 20 bills
    if (value >= 20):
        bills20 = value // 20
        value -= bills20 * 20
        print('USD 20 bills: {}' .format(bills20))
        if not value:
            break


    # verifies if there are USD 10 bills
    if (value >= 10):
        bills10 = value // 10
        value -= bills10 * 10
        print('USD 10 bills: {}' .format(bills10))
        if not value:
            break


    # verifies if there are USD 5 bills
    if (value >= 5):
        bills5 = value // 5
        value -= bills5 * 5
        print('USD 5 bills: {}' .format(bills5))
        if not value:
            break


    # verifies if there are USD 2 bills
    if (value >= 2):
        bills2 = value // 2
        value -= bills2 * 2
        print('USD 2 bills: {}' .format(bills2))
        if not value:
            break


    # verifies if there are USD 1 coins
    if (value >= 1):
        coins1 = value // 1
        value -= coins1 * 1
        print('USD 1 coins: {}' .format(coins1))
        if not value:
            break
