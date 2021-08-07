def valid_int(question, min, max):
    x = int(input(question))
    if (x < min) or (x > max):
        x = int(input(question))
    return x


#main program


x = valid_int('Type a valid value:', 0, 100)
print('You typed "{}". Valid number. Closing program...' .format(x))
