from random import randint

while True:
    try:
        level = int(input("Level: "))
    except ValueError:
        continue
    else:
        break
    
number = randint(1, level)

while True:
    try:
        guess = int(input("Guess: "))
    except ValueError:
        continue
    
    if guess > number:
        print("Too large!")
    elif guess < number:
        print("Too small!")
    elif guess == number:
        print("Just right!")
        break
