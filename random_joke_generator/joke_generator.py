# 😂 Random Joke Generator

import random

def joke_generator():
    jokes = [
        "Why don’t scientists trust atoms? Because they make up everything!",
        "I told my computer I needed a break, and it said 'No problem — I'll go to sleep.'",
        "Why did the scarecrow win an award? Because he was outstanding in his field!"
    ]

    print("😂 Here's a random joke for you:")
    print(random.choice(jokes))

if __name__ == "__main__":
    joke_generator()
