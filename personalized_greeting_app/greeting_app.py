

def personalized_greeting():
    print("👋 Welcome to the Personalized Greeting App!")

    name = input("What's your name? ")
    color = input("What's your favorite color? ")

    print(f"\nHello, {name.title()}! Your favorite color, {color.lower()}, is awesome! 🎨")

if __name__ == "__main__":
    personalized_greeting()
