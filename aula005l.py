#Function to return a string provided it is between a determined range of length via keyboard(input)
def valid_string(text, min, max):
    s1 = input(text)
    length = len(s1)
    while (length < min) or (length > max):
        s1 = input(text)
        length = len(s1)
    return s1

#Variable (x)  summoning the function valid_string
x = valid_string('Type a string:', 10, 30)

#Result the user is provided with
print('You typed the string "{}".\nValid value!\nClosing program...' .format(x))

