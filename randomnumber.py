import random
number = random.randint(1, 100)
counter = 0
print("Welcome to guess the number!")
username = input("Enter username: ")
while True:
    usernumber = int(input("Enter number: "))
    if usernumber == number:
        print("Congrats, the number has been guessed! Number of guesses:")
        print(counter)
        break
    elif usernumber < number:
        print("Too low.")
        counter+=1

    elif usernumber > number:
        print("Too high.")
        counter+=1