import random

def main():
    print('*' * 75)
    print('🎲 Game rules: 🎲')
    print('1. Role your dice - Select number between 1 to 6')
    print('2. Computer also roll a dice, If your dice number and computer dice number is same You Win!')
    print('3. If number is not same computer wins')
    print('4. Enter 0 to exit the game')

    playGame = input('Start game (y/n): ').lower()

    if playGame == 'y':
        startGame()
    elif playGame == 'n':
        print('Exited from game')
    else:
        print('Invalid Choice!')


def startGame():
    
    while True:
        try:
            playerNumber = int(input('Roll the dice 🎲: Select number between 1 - 6: '))

            if playerNumber == 0:
                print('Exited from game')
                break

            computerNumber = random.randint(1, 6)

            print(F'Your number: {playerNumber}')
            print(F'Computer number: {computerNumber}')

            if playerNumber == computerNumber:
                print('Congrats You Win! 🎉')
            else:
                print('You Lost! 😛')
        except ValueError:
            print('Enter a valid number')


if __name__ == '__main__':
    main()