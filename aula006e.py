def sum(*num):
    sum = 0
    print('Tuple: {}' .format(num))
    for i in num:
        sum += i
    return sum


print('Result: {}' .format(sum(1, 2)))
print('Result: {}' .format(sum(1, 2, 3, 4, 5, 6, 7, 8, 9)))
