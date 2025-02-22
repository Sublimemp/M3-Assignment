import random

def treasure_hunt():
    l = random.randint(5, 20)
    w = random.randint(5, 20)
    print(f"Grid dimensions: {l} (length) x {w} (width)")
    
    s1 = random.randint(1, w)
    s2 = random.randint(1, l)
    
    attempts = 0
    
    print("Try to find the treasure!")
    while True:
        try:
            x = int(input("Guess the row position of the treasure: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        
        attempts += 1
        if x < s1:
            print(f"You guessed too low for the row position, try again! {attempts} attempts used!")
        elif x > s1:
            print(f"You guessed too high for the row position, try again! {attempts} attempts used!")
        else:
            print(f"You guessed correctly! {attempts} attempts used, now try to guess the column position!")
            break
    
    while True:
        try:
            y = int(input("Guess the column position of the treasure: "))
        except ValueError:
            print("Invalid input. Please enter an integer.")
            continue
        
        attempts += 1
        if y < s2:
            print(f"You guessed too low for the column position, try again! {attempts} attempts used!")
        elif y > s2:
            print(f"You guessed too high for the column position, try again! {attempts} attempts used!")
        else:
            print(f"You guessed the position of the treasure correctly! {attempts} attempts used!")
            break

if __name__ == "__main__":
    treasure_hunt()
