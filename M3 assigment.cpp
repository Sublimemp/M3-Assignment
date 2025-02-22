import random

def treasure_hunt():
    l = random.randint(5, 10)
    w = random.randint(5, 10)
    s1 = random.randint(1, w)
    s2 = random.randint(1, l)
    attempts = 0

    print("Grid size:", w, "x", l)
    
    x = 0
    while x != s1:
        x = int(input("Guess the row: "))
        attempts += 1
        if x < s1:
            print("Too low!")
        elif x > s1:
            print("Too high!")
    
    print("Correct! Now guess the column.")
    
    y = 0
    while y != s2:
        y = int(input("Guess the column: "))
        attempts += 1
        if y < s2:
            print("Too low!")
        elif y > s2:
            print("Too high!")
    
    print("You found the treasure in", attempts, "attempts!")

treasure_hunt()

