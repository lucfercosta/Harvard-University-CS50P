from random import randint


def main():
    score = 0
    chances = 3
    level = get_level()

    for i in range(10):
        x, y = generate_integer(level)
        result = x + y
        
        while True:
            try:
                user_answer = int(input(f"{x} + {y} = "))
                if user_answer == result:
                    score += 1
                    break
            except ValueError:
                print("EEE")
                chances -= 1
                if chances < 1:
                    print(f"{x} + {y} = {result}")
                    chances = 3
                    break
    print(f"Score: {score}")
                
def get_level():
    while True:
        try:
            level = int(input("Level: "))
        except ValueError:
            continue
        if level == 1 or level == 2 or level == 3:
            return level
        else:
            continue
    
def generate_integer(level):
    if level == 1:
        x = randint(1, 9)
        y = randint(1, 9)
    elif level == 2:
        x = randint(10, 99)
        y = randint(10, 99)
    else:
        x = randint(100, 999)
        y = randint(100, 999)   
    return x, y

if __name__ == "__main__":
    main()