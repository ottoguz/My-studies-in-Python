#Program that creates a .txt file in case it does not exist and stores games and its console names


#Function to provide the user with the intructions to choose from an option adequate to the parameters

def valid_string(question, min, max):
    x = int(input(question))
    while (x < min) or (x > max):
        x = int(input(question))
    return x


#Function to check if the file already exists or needs to be created
def file_exists(file_name):
    try:
        f = open(file_name, 'rt') #rt = read text
        f.close()
    except FileNotFoundError:
        return False
    else:
        return True


#function that creates the .txt file
def create_file(file_name):
    try:
        f = open(file_name, 'wt+') #wt+ = create the file
        f.close()
    except:
        print('Error creating file!')
    else:
        print('File "{}" created successefully!\n' .format(file))


#Function that registers games and its consle names on the .txt file
def register_game(file_name, game_name, console_name):
    try:
        f = open(file_name, 'at')
    except:
        print('Error writing on file')
    else:
        f.write('Game name: {} | Console name: {}\n' .format(game_name, console_name))
    finally:
        f.close()


#Function that lists the registered games on the screen for the user
def list_file(file_name):
    try:
        f = open(file_name, 'rt')
    except:
        print('Error reading the file!')
    else:
        print(f.read())
    finally:
        f.close()


def binding(s1):
    size = len(s1)
    print('+' + '-' * size + '+')
    print('|' + s1 + '|')
    print('+' + '-' * size + '+')


#Point where the main program starts by verifying wheter the .txt exists
file = 'Games.txt'
if file_exists(file):
    print('File "{}" found on your computer!' .format(file))
else:
    create_file(file)



#A menu to make the program user-friendly
menu = 'MENU'
binding('{:*^20}'.format(menu))

print('1 - REGISTER GAME.')
print('2 - VIEW FILE.')
print('3 - LEAVE.')


#Repetition cycle in which data is processed and the program can e closed by pressing 3
while True:
    option = valid_string('Choose an option:', 1, 3)
    if option == 1:
        print('You chose the option "REGISTER GAME"!')
        game_name = str(input('Type in the game name:'))
        console_name = str(input('Type in the console name:'))
        register_game(file, game_name, console_name)

    elif option == 2:
        list_file(file)

    elif option == 3:
        print('Closing the program...')
        break




