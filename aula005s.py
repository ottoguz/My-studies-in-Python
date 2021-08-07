#Function that receives an integer via keyboard and determines the range(which should comprehend positive numbers)
def valid_int(question, min, max):
    x = int(input(question))
    if ((x < min) or (x > max)):
        x = int(input(question))
    return x

#Function to calculate the factorial of a given number
def factorial(num):
    """
    :param num: number to be factored as a parameter
    :return: returns the result of the factored number
    """
    fat = 1
    if num == 0:
        return fat
    for i in range(1, num + 1, 1):
        fat *= i
    return fat

# x = variable in which the function valid_int(question, min, max) is summoned
x = valid_int('Type in a factorial:', 0, 99999)
#result printed for the user
print('{}! = {}' .format(x, factorial(x)))
help(factorial)

