import random

def world_scramble():
    words = ["python", "Meat", "List", "algorithm", "Juice", "Drink", "Jacket", "Bloom", "Phone", "Wallet"]
    word = random.choice(words)
    scrambled = ''.join(random.sample(word, len(word)))
    
    print(f"Scrambled word: {scrambled}")
    guess = input("Guess the original word: ")
    
    if guess == word:
        print("Correct!")
    else:
        print(f"Wrong! The correct word was {word}.")
        
world_scramble()