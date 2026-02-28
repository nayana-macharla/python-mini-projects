# INTERACTIVE MADLIBS GENERATOR - YOU CHOOSE THE STORY!

import random

print("=" * 50)
print("🎭 WELCOME TO INTERACTIVE MADLIBS! 🎭")
print("=" * 50)

# Step 1: Ask what kind of story they want
print("\nWhat kind of story would you like to create?")
print("1. 👻 Scary Story")
print("2. 🤣 Funny Story")
print("3. 💕 Romantic Story")
print("4. 🚀 Sci-Fi Adventure")
print("5. 🎲 Random Surprise!")

# Get their choice
while True:
    choice = input("\nEnter your choice (1-5): ")
    if choice.isdigit() and 1 <= int(choice) <= 5:
        choice = int(choice)
        break
    else:
        print("Please enter a number between 1-5")

# Step 2: Get words based on their choice
print("\n📝 Great! Now give me some words:")

if choice == 1:  # Scary story
    adjective = input("Enter a scary adjective (e.g., creepy, haunted, dark): ")
    noun = input("Enter a scary noun (e.g., ghost, vampire, monster): ")
    verb = input("Enter a scary verb (e.g., lurking, haunting, screaming): ")
    place = input("Enter a scary place (e.g., cemetery, haunted house, cave): ")
    animal = input("Enter a scary animal (e.g., bat, wolf, spider): ")
    food = input("Enter a gross food (e.g., worms, eyeballs, moldy bread): ")
    
    story = f"""
    🌕 SCARY STORY 🌕
    
    It was a {adjective} night at the {place}. Suddenly, a {animal} appeared!
    It started {verb} near the old {noun}. I heard strange noises and saw {food} everywhere.
    
    The {noun} began to move! I tried to run, but a {adjective} figure blocked my way.
    
    TO BE CONTINUED... if you dare! 👻
    """

elif choice == 2:  # Funny story
    adjective = input("Enter a funny adjective (e.g., silly, wobbly, goofy): ")
    noun = input("Enter a funny noun (e.g., banana, clown, pickle): ")
    verb = input("Enter a funny verb (e.g., dancing, burping, juggling): ")
    place = input("Enter a funny place (e.g., bathroom, circus, supermarket): ")
    animal = input("Enter a funny animal (e.g., penguin, duck, monkey): ")
    food = input("Enter a silly food (e.g., spaghetti, jelly beans, pizza): ")
    
    story = f"""
    🤣 FUNNY STORY 🤣
    
    At the {place}, I saw a {adjective} {animal} trying to {verb} with a {food}!
    A {noun} walked by and started laughing so hard it fell down.
    
    Everyone was {verb} and having a {adjective} time. Even the {noun} joined in!
    
    What a {adjective} day at the {place}! 😂
    """

elif choice == 3:  # Romantic story
    adjective = input("Enter a romantic adjective (e.g., beautiful, lovely, sweet): ")
    noun = input("Enter a romantic noun (e.g., rose, heart, candle): ")
    verb = input("Enter a romantic verb (e.g., dancing, whispering, hugging): ")
    place = input("Enter a romantic place (e.g., beach, garden, Paris): ")
    animal = input("Enter a cute animal (e.g., bunny, dove, kitten): ")
    food = input("Enter a romantic food (e.g., chocolate, strawberries, wine): ")
    
    story = f"""
    💕 ROMANTIC STORY 💕
    
    Under the stars at the {place}, two {animal}s were {verb} together.
    They shared {food} while holding a {adjective} {noun}.
    
    The {adjective} evening was perfect. Even the {noun} seemed to glow!
    
    Love was in the air at the {place}. 💖
    """

elif choice == 4:  # Sci-Fi story
    adjective = input("Enter a sci-fi adjective (e.g., alien, futuristic, glowing): ")
    noun = input("Enter a sci-fi noun (e.g., spaceship, robot, laser): ")
    verb = input("Enter a sci-fi verb (e.g., teleporting, beaming, cloning): ")
    place = input("Enter a sci-fi place (e.g., Mars, space station, galaxy): ")
    animal = input("Enter an alien animal (e.g., Martian, space lizard, alien cat): ")
    food = input("Enter a space food (e.g., space chips, alien goo, planet powder): ")
    
    story = f"""
    🚀 SCI-FI ADVENTURE 🚀
    
    On the {place}, a {adjective} {animal} was {verb} with a {noun}.
    They ate {food} while exploring the {adjective} landscape.
    
    Suddenly, a giant {noun} appeared! Time to {verb} back to Earth!
    
    To infinity and beyond! 🌟
    """

else:  # Random - mix of all themes
    print("\n🎲 RANDOM SURPRISE! Mixing everything!")
    adjective = input("Enter any adjective: ")
    noun = input("Enter any noun: ")
    verb = input("Enter any verb: ")
    place = input("Enter any place: ")
    animal = input("Enter any animal: ")
    food = input("Enter any food: ")
    
    # Random story starter
    starters = [
        f"At the {place}, a {adjective} {animal} was {verb}...",
        f"Suddenly, a {noun} appeared at the {place}!",
        f"The {animal} loved to {verb} with {food}...",
        f"In a {adjective} world, the {noun} ruled..."
    ]
    
    story = f"""
    🎲 RANDOM SURPRISE STORY! 🎲
    
    {random.choice(starters)}
    
    Everyone was {verb} while eating {food}. The {adjective} {noun} watched from {place}.
    
    Even the {animal} couldn't believe what happened next!
    
    The end... or is it? 🤔
    """

# Step 3: Show the story
print("\n" + "=" * 50)
print("📖 YOUR CUSTOM MADLIBS STORY 📖")
print("=" * 50)
print(story)
print("=" * 50)
print("\nThanks for playing! Want to try another theme? Run the program again! 🎉")