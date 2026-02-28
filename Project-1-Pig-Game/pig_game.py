# PIG DICE GAME - PROJECT 1
import random

def roll():
    return random.randint(1, 6)

# Get number of players
while True:
    players = input("Enter the number of players (2-4): ")
    if players.isdigit():
        players = int(players)
        if 2 <= players <= 4:
            break
        else:
            print("Must be between 2-4 players.")
    else:
        print("Invalid input. Please enter a number.")

print(f"Game starting with {players} players!")

# Initialize scores
player_scores = [0 for _ in range(players)]

# Game loop
while max(player_scores) < 50:
    for player_idx in range(players):
        print(f"\nPlayer {player_idx + 1}'s turn! Total score: {player_scores[player_idx]}")
        current_score = 0
        
        while True:
            should_roll = input("Would you like to roll (y)? ")
            if should_roll.lower() != "y":
                break
            
            value = roll()
            if value == 1:
                print("You rolled a 1! Turn over, no points added.")
                current_score = 0
                break
            else:
                current_score += value
                print(f"You rolled a: {value}")
                print(f"Your turn score is: {current_score}")
        
        player_scores[player_idx] += current_score
        print(f"Player {player_idx + 1}'s total score is now: {player_scores[player_idx]}")

# Winner
max_score = max(player_scores)
winning_idx = player_scores.index(max_score)
print(f"\nPlayer {winning_idx + 1} wins with {max_score} points!")
