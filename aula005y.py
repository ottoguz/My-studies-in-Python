def valid_int(question, min, max):
    x = int(input(question))
    while (x < min) or (x > max):
        x = int(input(question))
    return x

def sum_interval(start, end):
    sum = 0
    i = start
    while i <= end:
        sum += i
        i += 1
    return sum


#main program


x = valid_int('Type in a positive integer:', 1, 999999)
y = valid_int('Type in a second positive integer:', 1, 99999)
print('The somatory between "{}" and "{}" is: {}'. format(x, y, sum_interval(x, y)))


