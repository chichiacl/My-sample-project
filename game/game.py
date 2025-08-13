import random

while True:
    try:
        level = int(input("Level: "))
        if level <= 0:
            continue
        else:
            break
    except ValueError:
        continue

integer = random.randint(1,level)

while True:
    try:
        guess = int(input("Guess: "))
        if guess <= 0:
            continue
        elif guess < integer:
            print("Too small!")
        elif guess > integer:
            print("Too large!")
        else:
            print("Just right!")
            break
    except ValueError:
        continue





