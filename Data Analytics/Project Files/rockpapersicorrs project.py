# Write your code here :-)
import random, sys
print ('Rock, Paper, Scissors')

#these variables keep track of the number of wins losses and ties
wins = 0
losses = 0
ties = 0

while True: #main game loop
    print('%s Wins, %s Losses, %s Ties' % (wins, losses, ties))
    while True: #the player input loop
        print('Enter your move: (r)ock (p)aper (s)cissors or (q)uit')
        playerMove = input()
        if playerMove == 'q':
            sys.exit('You are a quiter') #Quit the game
        if playerMove == 'r' or playerMove == 'p' or playerMove == 's':
            break   #break ouf of the player input loop
        print('Type one of r, p, s, or q.')

    #Display what the player chose
    if playerMove == 'r':
        print('ROCK versus...')
    elif playerMove == 'p':
        print('PAPER versus...')
    elif playerMove == 's':
        print('Scissors versus...')

    #Display what the computer chose
    import random
    randomNumber = random.randint(1,3)
    if randomNumber == 1:
        computerMove = 'r'
        print('ROCK')
    elif randomNumber == 2:
        computerMove = 'p'
        print('PAPER')
    elif randomNumber == 3:
        computerMove = 's'
        print('Scissors')

    #Display and record the win/loss/ties
    if playerMove == computerMove:
        print('It is a tie')
        ties = ties + 1
    elif playerMove == 'r' and computerMove == 's':
        print('You Win!')
        wins = wins + 1
    elif playerMove == 'p' and computerMove == 'r':
        print('You Win!')
        wins = wins + 1
    elif playerMove == 's' and computerMove == 'p':
        print('You Win!')
        wins = wins + 1
    elif playerMove == 'r' and computerMove == 'p':
        print('You Lose!')
        losses = losses + 1
    elif playerMove == 'p' and computerMove == 's':
        print('You Lose!')
        losses = losses + 1
    elif playerMove == 's' and computerMove == 'r':
        print('You Lose!')
        losses = losses +1









