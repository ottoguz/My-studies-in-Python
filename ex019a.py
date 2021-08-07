#Randomizer with 4 names
import random
n1 = str(input('1° ALuno:'))
n2 = str(input('2° ALuno:'))
n3 = str(input('3° ALuno:'))
n4 = str(input('4° ALuno:'))
list = [n1, n2, n3, n4]
chosen = random.choice(list)
print('O aluno escolhido foi {}.' .format(chosen))



