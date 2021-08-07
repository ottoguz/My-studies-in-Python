#READ A NUMBER BETWEEN 0 AND 9999 AND SAY HOW MANY THOUSANDS, HUNDREDS, TENS AND UNITS THERE ARE(via string)
numero = input('DIgite um número entre 0 e 9999:')
print('Milhares: {}\n' .format(numero.split()[0][0]))
print('Centenas: {}\n' .format(numero.split()[0][1]))
print('Dezenas: {} \n' .format(numero.split()[0][2]))
print('Unidades: {}' .format(numero.split()[0][3]))

