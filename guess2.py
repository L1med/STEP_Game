import random
low=1
high=100
mid=(low+high)/2
number=random.randint(low, high)
counter=0
print("Welcome to guess the number!")
username = input("Enter username: ")
while True:
    if number==mid:
        print("Number has been chosen")
        break
    elif number<mid:
        print(counter)
        high=mid-1
        mid=(low+high)/2

    else:
        print(counter)
        low=mid+1
        mid=(low+high)/2