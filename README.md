# Deal or No Deal
The code for the "Deal or No Deal Game I created" I used Python and an OOP framework

The game "deal or no deal" is a game where the player starts by choosing one numbered case out of 26 cases. All cases hold a monetary value. The values range from $0.01 to $1,000,000 

The player inputs the number of the case they want to pick. Input validity was checked using regexes, and all invalid inputs will be caught.

There are several rounds for the game, and in each round you pick different numbers of cases to be eliminated from the game. The goal of the game is to pick a case with the most money, or, make a deal to sell your case with the banker. After each round, the banker calls in to make a deal. You can accept the deal, deny it, or provide a counter offer. 

The equation I found to calculate the value of the deal the banker offers was found online. On the actual game show, there are several factors that could change the amount of money offered by the banker. To keep it more simple, this formula is a decent approximation.

If you counter offer, the banker can accept or deny it. I couldn't find the actual game's requirements for the banker accepting a counter offer, so, if you counteroffer with a value that's 20% more than the original deal offered, the banker will accept.

If you accept a deal, or the banker accepts a counter offer, the game ends.

If you make it to the final round, you have the option to keep the value in your original case, or, swap it with the one remaining case. You win the value of the case you decide to go with.

I play tested the game as I created it, and the game works fine. I did not complete any unit tests for the program.

Requirements:
Python

