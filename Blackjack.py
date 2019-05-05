from random import shuffle
from IPython.display import clear_output

def deck():
    
    deck = []
    numbers = [1,2,3,4,5,6,7,8,9,10,11,12,13]
    suit = ['Hearts','Diamonds','Spades','Clubs']

    for i in suit:
        for j in numbers:
            deck.append((i, j)) #This adds tuples to your deck
            
    shuffle(deck)
        
    return deck

#Create a point system to to show card values from 1-13.
def pointSystem(cards):

    count = 0

    for i in cards:
        count += (i[1])
    return count

#Create a method for the Dealer and Player points
def PlayerDealerHands(mCards):

    #empty lists for player and dealer hand
    player_hand = []
    dealer_hand = []

    #Gives two random cards to the player and dealer hand
    player_hand.append(mCards.pop())
    player_hand.append(mCards.pop())
    dealer_hand.append(mCards.pop())
    dealer_hand.append(mCards.pop())

    while (pointSystem(dealer_hand) <= 16):
            dealer_hand.append(mCards.pop())
    return [dealer_hand,player_hand]


#total number of cards or the deck
mCards = deck()

#the player and dealers hands
hands = PlayerDealerHands(mCards)

dealer = hands[0]
player = hands[1]


#Create game logic here - this will compare the dealer card count vs. player card count
while True:

        #initiate game play here
        game = input('Would you like to play BlackJack? ')

        if game == 'yes':

            #This is the tally system for dealer and player, will be comparing the two
            dealer_count = pointSystem(dealer)
            player_count = pointSystem(player)
            
            print('Dealer has:')
            print(dealer[0])
            
            print('You have: ')
            print(player)

            #blackjack scenario
            if player_count == 21:
                print('BlackJack, You win')
                break
                
            if player_count == 21 and dealer_count == 21:
                print('PUSH Result, you and the dealer both have ' + str(player_count))
                break


            #player gets over 21 
            elif player_count > 21:
                print('Player Bust, you lose because you have ' + str(player_count))
                break

            #dealer gets over 21
            elif dealer_count > 21:
                print('Dealer Bust with: ' + str(dealer_count))
                break
                
            #ask to keep hitting or not
            answer = input('Would you like to Hit or Stand? ')

            #add another random number to player hannd
            while True: 
                if answer == 'Hit':
                    
                    player.append(mCards.pop())
                    print(player)

                    if (player_count > dealer_count):
                        print('You are closer to 21, you win with: ' + str(player_count))
                        print('Dealer has: ' + str(dealer))
                        break

                    elif (dealer_count > player_count):
                        print('Dealer is closer to 21, you lose')
                        print('Dealer has: ' + str(dealer) )
                        break

                #compare the player and dealer counts to see who is closest to 21
                elif answer == 'Stand' and (player_count > dealer_count):
                        print('You are closer to 21, you win with: ' + str(player_count))
                        print('Dealer has: ' + str(dealer))
                        break

                else:
                    print('Dealer is closer to 21, you lose')
                    print('Dealer has: ' + str(dealer) )
                    break

        else:
            print('You decided not to play!')
            break