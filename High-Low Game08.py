import random

def play_round():
    player_number = random.randint(1, 100)
    computer_number = random.randint(1, 100)
    print(f"Your number is {player_number}")
    
    guess = input("Do you think your number is higher or lower than the computer's number? (say 'Higher' or 'Lower'): ").lower()
    
    if (guess == "higher" and player_number > computer_number) or (guess == "lower" and player_number < computer_number):
        print(f"Correct! The computer's number was {computer_number}. You got a point!")
        return 1
    else:
        print(f"Wrong! The computer's number was {computer_number}. No point.")
        return 0

def play_game(rounds):
    score = 0
    for i in range(rounds):
        print(f"Round {i + 1}")

        print("\nStarting a new round....")
        score += play_round()
    
    print(f"Game over! Your total score is: {score}")

# Get the number of rounds from the player
rounds_to_play = int(input("How many rounds would you like to play? "))  
play_game(rounds_to_play)
   
