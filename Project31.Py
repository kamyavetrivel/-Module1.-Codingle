import requests

url = "https://uselessfacts.jsph.pl/api/v2/facts/random"

def get_fact():
    response = requests.get(url)

    if response.status_code == 200:
        data = response.json()
        print(data["text"])
    else:
        print("Failed to get fact")

while True:
    answer = input("Press Enter for a fact or q to quit: ")

    if answer.lower() == "q":
        break

    get_fact()
