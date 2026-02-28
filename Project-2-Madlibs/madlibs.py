# MADLIBS GENERATOR - PROJECT 2
import random

print("=" * 50)
print("WELCOME TO INTERACTIVE MADLIBS!")
print("=" * 50)

print("\nWhat kind of story would you like?")
print("1. Scary Story")
print("2. Funny Story")
print("3. Romantic Story")
print("4. Sci-Fi Adventure")
print("5. Random Surprise!")

while True:
    choice = input("\nEnter your choice (1-5): ")
    if choice.isdigit():
        choice = int(choice)
        if 1 <= choice <= 5:
            break
        else:
            print("Please enter 1-5")
    else:
        print("Please enter a number")

print("\nGreat! Give me some words:")

if choice == 1:  # Scary
    adjective = input("Enter a scary adjective: ")
    noun = input("Enter a scary noun: ")
    verb = input("Enter a scary verb: ")
    place = input("Enter a scary place: ")
    animal = input("Enter a scary animal: ")
    food = input("Enter a gross food: ")
    
    story = f"""
    SCARY STORY
    
    It was a {adjective} night at the {place}. Suddenly, a {animal} appeared!
    It started {verb} near the old {noun}. I saw {food} everywhere.
    The {noun} began to move! A {adjective} figure blocked my way.
    TO BE CONTINUED... if you dare!
    """

elif choice == 2:  # Funny
    adjective = input("Enter a funny adjective: ")
    noun = input("Enter a funny noun: ")
    verb = input("Enter a funny verb: ")
    place = input("Enter a funny place: ")
    animal = input("Enter a funny animal: ")
    food = input("Enter a silly food: ")
    
    story = f"""
    FUNNY STORY
    
    At the {place}, I saw a {adjective} {animal} trying to {verb} with {food}!
    A {noun} walked by and laughed so hard it fell down.
    Everyone was having a {adjective} time!
    What a {adjective} day at the {place}!
    """

elif choice == 3:  # Romantic
    adjective = input("Enter a romantic adjective: ")
    noun = input("Enter a romantic noun: ")
    verb = input("Enter a romantic verb: ")
    place = input("Enter a romantic place: ")
    animal = input("Enter a cute animal: ")
    food = input("Enter a romantic food: ")
    
    story = f"""
    ROMANTIC STORY
    
    Under the stars at the {place}, two {animal}s were {verb} together.
    They shared {food} while holding a {adjective} {noun}.
    The {adjective} evening was perfect. Love was in the air!
    """

elif choice == 4:  # Sci-Fi
    adjective = input("Enter a sci-fi adjective: ")
    noun = input("Enter a sci-fi noun: ")
    verb = input("Enter a sci-fi verb: ")
    place = input("Enter a sci-fi place: ")
    animal = input("Enter an alien animal: ")
    food = input("Enter space food: ")
    
    story = f"""
    SCI-FI ADVENTURE
    
    On {place}, a {adjective} {animal} was {verb} with a {noun}.
    They ate {food} while exploring the {adjective} landscape.
    Suddenly, a giant {noun} appeared! Time to {verb} back to Earth!
    To infinity and beyond!
    """

else:  # Random
    print("\nRandom Surprise!")
    adjective = input("Enter any adjective: ")
    noun = input("Enter any noun: ")
    verb = input("Enter any verb: ")
    place = input("Enter any place: ")
    animal = input("Enter any animal: ")
    food = input("Enter any food: ")
    
    starters = [
        f"At {place}, a {adjective} {animal} was {verb}...",
        f"Suddenly, a {noun} appeared at {place}!",
        f"The {animal} loved to {verb} with {food}...",
    ]
    
    story = f"""
    RANDOM STORY
    
    {random.choice(starters)}
    
    Everyone was {verb} while eating {food}.
    The {adjective} {noun} watched from {place}.
    The end... or is it?
    """

print("\n" + "=" * 50)
print("YOUR MADLIBS STORY")
print("=" * 50)
print(story)
print("=" * 50)
print("\nThanks for playing! Run again for another story!")
