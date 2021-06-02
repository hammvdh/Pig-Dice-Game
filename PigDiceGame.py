import random
import time

#initializing variables

player1total=0
player2total=0
player3total=0
player4total=0

turn_total_1=0 # for player 1
turn_total_2=0 # for player 2
turn_total_3=0 # for player 3
turn_total_4=0 # for player 4

# Function to announce the winner and total score

def winners():
    global winner
    time.sleep(1)
    print('Game has ended')
    print('\n')
    print('The Winner is ',winner)
    print('Congratulations!')
    print('\n')
    time.sleep(1)
    print('*'*22)
    print('*'*4,'Total Score','*'*4)
    print('*'*20)
    if players==2:
        print('Player 1 - ',player1total)
        print('Player 2 - ',player2total)
    if players==3:
        print('Player 1 - ',player1total)
        print('Player 2 - ',player2total)
        print('Player 3 - ',player3total)
    if players==4:
        print('Player 1 - ',player1total)
        print('Player 2 - ',player2total)
        print('Player 3 - ',player3total)
        print('Player 4 - ',player4total)
    exit()

#Function to ask for number of players

def playerss():
    global players
    try:
        players=int(input('How many players? - (2,3,4) : '))
        if players>4 or players<2:
            print('Sorry,minimum players are 2, maximum players are 4')
            playerss()
    except:
        print('Sorry, only integer input - minimum players are 2, maximum players are 4')
        playerss()

playerss()

time.sleep(1)

print('First to 100 score wins')

time.sleep(1)

print('Player One goes first')

time.sleep(1)

#player 2 is put before player 1 so that it can be called once player1's turn is done

def player2():
    
    global turn_total_2,player2total, winner # creating global variables to be use in the function
    
    print("Player 2's Turn")
    
    rollagain=str(input('Do you want to roll the dice or hold your score - respond with one of the following (roll,hold): '))
    
    if rollagain=='roll':
        while rollagain=='roll':
            print('rolling dice...')
            
            time.sleep(1)
            
            dice=random.randint(1,6)
            print('you rolled a',dice)
            

            if dice==1:
                print('since you rolled a 1, you lose your turn_total_ for this turn')
                turn_total_2=0
                if players==2:
                    print('\n')
                    player1()
                elif players==3 or players==4:
                    print('\n')
                    player3()
                break
            
            print('\n')
            turn_total_2 = turn_total_2 + dice
            rollagain=str(input('Do you want to roll the dice or hold your score - respond with one of the following(roll,hold): '))
                
        if rollagain=='hold':
            print('you are holding your score ')
            player2total=player2total+turn_total_2
            print('\n')
            print('your total score now is ',player2total)
            
            if player2total>=100:
                winner=('Player 2')
                winners()
                
            time.sleep(1)
            print('now its the next players turn')
            
            turn_total_2=0
            
            if players==2:
                    player1()
            elif players==3 or players==4:
                    player3()

        else:
            print('\n')
            print('Sorry,your score is reset - please reply with accepted values only (roll, hold)')
            
            player2()

def player1():
    global turn_total_1,player1total,winner
    
    print ("Player 1's turn")
    
    rollagain = str(input('Do you want to roll the dice or hold your turn_total_ - respond with one of the following (roll,hold): '))
    
    if rollagain =='roll':
        while rollagain =='roll':
            
            print('rolling dice...')
            time.sleep(1)
            
            dice=random.randint(1,6)
            print('you rolled a',dice)

            if dice == 1:
                
                print('since you rolled a 1, you lose your score for this turn')
                print('\n')
                
                time.sleep(1)
                
                turn_total_1 = 0

                player2()
                
                break
            
            turn_total_1 += dice # adding points to turn total
            
            print('\n')
            rollagain=str(input('Do you want to roll the dice or hold your score - respond with one of the following(roll,hold): '))
                
        if rollagain=='hold':
            print('you are holding your score ')
            
            player1total+=turn_total_1
            
            print('your total score now is ',player1total)

            if player1total>=100:
                winner=('Player 1')
                winners()
            time.sleep(1)
            print('\n')
            turn_total_1 = 0
            player2()

        else:
            print('\n')
            print('Sorry, please reply with an accepted value (roll, hold)')
            player1()
            
    if rollagain=='hold':
        print('Sorry but you need minimum 1 roll to hold')
        print('Lets try that again!')
        print('\n')
        time.sleep(1)
        player1()

def player3():
    global turn_total_3,player3total,winner
    print("Player 3's Turn")
    rollagain=str(input('Do you want to roll the dice or hold your turn_total_ - respond with one of the following (roll,hold): '))
    if rollagain=='roll':
        while rollagain=='roll':
            print('rolling dice...')
            time.sleep(1)
            dice=random.randint(1,6)
            print('you rolled a',dice)
            

            if dice==1:
                print('since you rolled a 1, you lose your turn_total_ for this turn')
                turn_total_3=0
                if players==3:
                    player1()
                elif players==4:
                    player4()
                break
            
            print('\n')
            turn_total_3=turn_total_3+dice
            rollagain=str(input('Do you want to roll the dice or hold your turn_total_ - respond with one of the following(roll,hold): '))
                
        if rollagain=='hold':
            print('you are holding your turn_total_ ')
            player3total = player3total + turn_total_3
            print('\n')
            print('your total turn_total_ now is ',player3total)
            
            if player3total>=100:
                winner=('Player 3')
                winners()
                
            time.sleep(1)
            
            print('now its the next players turn')
            turn_total_3=0
            
            if players==3:
                    player1()
            elif players==4:
                    player4()

def player4():
    global turn_total_4,player4total,winner
    print("Player 3's Turn")
    rollagain=str(input('Do you want to roll the dice or hold your turn_total_ - respond with one of the following (roll,hold): '))
    if rollagain=='roll':
        while rollagain=='roll':
            print('rolling dice...')
            time.sleep(1)
            dice=random.randint(1,6)
            print('you rolled a',dice)
            
            if dice==1:
                print('since you rolled a 1, you lose your turn_total_ for this turn')
                turn_total_3=0
                player1()

                break
            print('\n')
            turn_total_4=turn_total_4+dice
            rollagain=str(input('Do you want to roll the dice or hold your turn_total_ - respond with one of the following(roll,hold): '))
                
        if rollagain=='hold':
            print('you are holding your turn_total_ ')
            
            player4total=player4total+turn_total_4
            
            if player4total>=100:
                winner=('Player 4')
                winners()
                
            print('\n')
            print('your total turn_total_ now is ',player4total)
            time.sleep(1)
            print('now its the next players turn')
            turn_total_3=0
            player1()

player1() # this is the initializer that starts the game from player 1

    
