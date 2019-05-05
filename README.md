#This is a game of BlackJack

# 1 We start off by importing two libraries, one for random - creates the random number/card pics and the other for shuffling the deck

# 2 We create the deck() method to consider 1-13 cards with the 4 card types - Hearts/Clubs/Diamonds/Spades
   # we add these numbers and suits to an empty list by appending them as tuples

# 3 We then add a points system with the method pointSystem, this will print out numbers 1-13 to both dealer and player hands

# 4 The next method is the PlayerDealerHands will append two random cards to the dealer and player, while keeping of the dealers cards secret.
 # there is a while loop that says, if the dealers hand is less than 16, he will automatically hit the next time.

 # 5 Finally, we start our game asking if they want to play, if so, the dealercount and playercount will automatically produce two cards for each.
# If the player gets 21 on the first try, its a blackjack and he wins, but not for the dealer
# if both dealer and player get 21 then the player wins
# If either dealer or player get over 21, they will bust/lose the game

# IF there are conditions where we want to keep hitting one of the two players passes 21