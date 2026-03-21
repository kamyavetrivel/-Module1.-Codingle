import random
from colorama import Fore, init

init(autoreset=True)

def chat():
    print(Fore.CYAN + "Hello! I am TravelBot")
    name = input("Your name: ")
    print(f"Hi {name}!")

    while True:
        user = input("You: ").strip().lower()

        if "recommend" in user:
            print("Do you like beaches, mountains, or cities?")
            choice = input("You: ").strip().lower()

            if "beach" in choice:
                print("Try Bali or Maldives")
            elif "mountain" in choice:
                print("Try Himalayas or Alps")
            elif "city" in choice:
                print("Try Paris or Tokyo")
            else:
                print("I don't know that option")

        elif "pack" in user:
            print("Pack light, bring a charger, and check the weather!")

        elif "joke" in user:
            jokes = [
                "Why don't programmers like nature? Too many bugs!",
                "Why did the computer go to the beach? To surf the web!",
                "Why was the robot tired? It had too many bytes!"
            ]
            print(random.choice(jokes))

        elif "help" in user:
            print("You can type: recommend, pack, joke, or exit")

        elif "exit" in user:
            print("Goodbye!")
            break

        else:
            print("I don't understand. Type 'help' to see options.")

# Run the chatbot
if __name__ == "__main__":
    chat()
