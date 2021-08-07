from random import randint
from time import sleep
while True:
    computer = randint(1, 5)
    print('-=' * 25)
    print('I will think about a number between 0 e 5...Try to guess...')
    print('-=' * 25)
    player = int(input('Qual número eu pensei?'))
    print('PROCESSANDO...')
    sleep(2)
    if player == computer:
        print('CONGRATULATIONS, YOU WIN!')
    else:
        print('I WIN! I THOUGHT OF THE NUMBER: {}. NOT THE NUMBER: {}.' .format(computer, player))


