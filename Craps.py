import random
import sys

#global variables
money = 100
point = 0
bet = 0

#instructions
def instructions():
    print('==================================')
    print('1. player rolls two six-sided dice and adds the numbers rolled together.')
    print('2. On this first roll, a 7 or an 11 automatically wins, and a 2, 3, or 12 automatically loses, and play is over.')
    print("If a 4, 5, 6, 8, 9, or 10 are rolled on this first roll, that number becomes the 'point.'")
    print("3. The player continues to roll the two dice again until one of two things happens:")
    print("either they roll the 'point' again, in which case they win; or they roll a 7, in which case they lose.")

#start menu
def startmenu():
    print("==========================")
    print("Welcome to Craps!")
    print('What do you want to do?')
    print('Balance: $%d' % (money))
    print('1. Play')
    print('2. Instructions')
    print('3. Quit')
    
    try:
        choice = int(input('Enter Choice: '))

        if choice in (1,2,3):
            return choice
        
        else:
            print("Invalid Choice.")
            main()
        
    except:
        print("Invalid Choice.")
        main()
        
    
 #diceroll   
def roll():

    die1 = random.randrange(1, 7)
    die2 = random.randrange(1, 7)
    plus = die1 + die2

    return plus

#Play menu
def playmenu():
    global money
    money = money
    #play menu

    
    print("==========================")
    print("Let's play some Craps!")
    print('A win pays 2 to 1 odds.\n')
    print('Balance: $%d' % (money))
    print('How much would you like to bet?')
        

#player chooses bet
def getbet():
    global bet
    bet = bet
    try:
        bet = int(input("Bet Amount: "))

        if bet < 1 or bet > money:
            print("bet must be a # between $1 and $%d" % (money))
            getbet()
        

    except ValueError:
        print("bet must be a # between $1 and $%d" % (money))
        getbet()

    return bet

#determines first roll
#win
#lose
#point
def firstroll():
    global money
    money = money
    global point
    point = point

    result = "r"

    input('Press Enter to roll!')
    throw = roll()
    print('You rolled ', throw)

    if throw in (7,11):
        result = "w"

    elif throw in (2,3,12):
        result = "l"

    else:
        result = "p"
        point = throw
        print("---------------------")
        print("The Point is now " , point)
        print("---------------------")
        

    return result

#display win
def win():
    global money
    money = money
    global bet
    bet = bet
    
    money = money + bet
    print("==========================")
    print("You Won!")
    print("Balance is now $%d" % (money))

#display loss
def lose():
    global money
    money = money
    global bet
    bet = bet
    
    money = money - bet
    print("==========================")
    print("Crapped out :(")
    print("balance is now $%d" % (money))

        
#rolling for the point
#if won on first roll ignore point rolling
def pointroll(result):
    while result == "p":
        print(" The Point is " , point)
        input('Press Enter to roll!')
        print('--------------------')
        
        throw = roll()
        print('You rolled ', throw)
        
        if throw == point:
            result = "w"

        elif throw == 7:
            result = "l"
            
    if result == "w":
        win()

    elif result == "l":
        lose()

#Play again
def playagain():
    if money < 1:
        print('You are BROKE!')
        input('Press Enter to exit...')
        sys.exit()
        
    print("would you like to play again?")
    again = input("choose y for yes anything else for no:")

    if again != "y":
        input('Press Enter to exit...')
        sys.exit()
        
    else:
        main()
    
#main
def main():
    
    if money < 1:
        print('You are BROKE!')
        input('Press Enter to exit...')
        quit()
        
    choice = startmenu()
    
    if choice == 1:
        playmenu()
        
        bet = getbet()

        pointroll(firstroll())

    elif choice == 2:
        instructions()
        main()

    elif choice == 3:
        print('See ya next time!')
        input('Press Enter to exit...')
        sys.exit()

    playagain()

main()

