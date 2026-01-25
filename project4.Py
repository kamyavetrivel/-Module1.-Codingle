import random 
numbers = [10, 20, 30, 40, 50] 
print("The list is",numbers)
numbers = random.choice(numbers)

guess = int(input("Guess a number from the list: "))


if guess > numbers:
    print("Your guess is higher than the original number.")
elif guess < numbers:
    print("Your guess is smaller than the original number.")
else:
    print("Correct guess! Well done ")