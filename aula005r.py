#Creating a help function
def sum3(x=0, y=0, z=0):
    """

    :param x:opitional integer value
    :param y:opitional integer value
    :param z:opitional integer value
    :return:Total of integer
    """
    return(x + y + z)

print(sum3(1, 2, 3))
help(sum3)

