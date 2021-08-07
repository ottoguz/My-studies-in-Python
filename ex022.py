#PROGRAM WHICH READS A PERSONS FULL NAME

#PRINTE COM LETRAS MINUSCULAS
#QTAS LETRAS S/ ESPAÇO
#QUANTAS LETRAS TEM O PRIMEIRO NOME

name = str(input('Type in your full name:')).strip()
size = len(name)

#Print with upper case letters
print('Your full name in upper case is: {}'.format(name.upper()))

#Print with lower case letters
print('Your name in lower case is: {}'.format(name.lower()))

#Number of letters without space
print('Your full name has {} letters'.format((size) - name.count(' ')))

#Print first name
print('Your first ame is: {}'.format(name.split()[0]))

#Print the number of letters in the first name
print('Your first name has {} letters.' .format(name.find(' ')))
print('Your first name has {} letters (Using the method split)'.format(len(name.split()[0])))



