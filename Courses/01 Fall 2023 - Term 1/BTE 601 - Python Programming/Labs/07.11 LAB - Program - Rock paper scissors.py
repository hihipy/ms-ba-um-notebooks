'''
7.11 LAB*: Program: Rock paper scissors
Program Specifications Write a program to play an automated game of Rock, Paper, Scissors. Two players make one of three hand signals at the same time. Hand signals represent a rock, a piece of paper, or a pair of scissors. Each combination results in a win for one of the players. Rock crushes scissors, paper covers rock, and scissors cut paper. A tie occurs if both players make the same signal. Use a random number generator of 0, 1, or 2 to represent the three signals.

Note: this program is designed for incremental development. Complete each step and submit for grading before starting the next step. Only a portion of tests pass after each step but confirm progress.

Step 0. Read starter template and do not change the provided code. Variables are defined for ROCK, PAPER, and SCISSORS. A seed is read from input to initialize the random number generator. This supports automated testing and creates predictable results that would otherwise be random.

Step 1 (2 pts). Read two player names from input (str). Read number of rounds from input. Continue reading number of rounds if value is below one and provide an error message. Output player names and number of rounds. Submit for grading to confirm 2 tests pass.
Ex: If input is:

3
Anna
Bert
-3
-4
4
Sample output is:

Rounds must be > 0
Rounds must be > 0
Anna vs Bert for 4 rounds

Step 2 (2 pts). Use random.randint(0, 2) to generate random values (0 - 2) for player 1 followed by player 2. Continue to generate random values for both players until both values do not match. Output "Tie" when the values match. Submit for grading to confirm 3 tests pass.
Ex: If input is:

12
Anna
Bert
1
Sample output is:

Anna vs Bert for 1 rounds
Tie
Tie

Step 3 (3 pts). Identify winner for this round and output a message. Rock crushes scissors, scissors cut paper, and paper covers rock. Submit for grading to confirm 6 tests pass.
Ex: If input is:

55
Anna
Bert
1
Sample output is:

Anna vs Bert for 1 rounds
Tie
Bert wins with rock

Step 4 (3 pts). Add a loop to repeat steps 2 and 3 for the number of rounds. Output total wins for each player after all rounds are complete. Submit for grading to confirm all tests pass.
Ex: If input is:

82
Anna
Bert
3
Sample output is:

Anna vs Bert for 3 rounds
Bert wins with paper
Anna wins with scissors
Tie
Anna wins with scissors
Anna wins 2 and Bert wins 1
'''

import random

ROCK = 0
PAPER = 1
SCISSORS = 2

# Read random seed to support testing (do not alter) and starting credits
seed = int(input())
# Set the seed for random
random.seed(int(seed))

# Step 1: Read names and number of rounds
player1_name = input()
player2_name = input()

# Continue reading number of rounds if value is below one and provide an error message
rounds = int(input())
while rounds < 1:
    print("Rounds must be > 0")
    rounds = int(input())

print(f"{player1_name} vs {player2_name} for {rounds} rounds")

# Step 4: Repeat steps 2 and 3 for the number of rounds
player1_wins = 0
player2_wins = 0

for i in range(rounds):
    # Step 2: Generate random values for both players until they do not match
    player1_choice = random.randint(0, 2)
    player2_choice = random.randint(0, 2)
    
    while player1_choice == player2_choice:
        print("Tie")
        player1_choice = random.randint(0, 2)
        player2_choice = random.randint(0, 2)
    
    # Step 3: Identify winner for this round
    if (player1_choice == ROCK and player2_choice == SCISSORS) or \
       (player1_choice == PAPER and player2_choice == ROCK) or \
       (player1_choice == SCISSORS and player2_choice == PAPER):
        print(f"{player1_name} wins with", end=" ")
        if player1_choice == ROCK:
            print("rock")
        elif player1_choice == PAPER:
            print("paper")
        else:
            print("scissors")
        player1_wins += 1
    else:
        print(f"{player2_name} wins with", end=" ")
        if player2_choice == ROCK:
            print("rock")
        elif player2_choice == PAPER:
            print("paper")
        else:
            print("scissors")
        player2_wins += 1

# After all rounds, output total wins for each player
print(f"{player1_name} wins {player1_wins} and {player2_name} wins {player2_wins}")