def guess():
    target = int(input("Enter the integer for the player to guess:\n"))
    attempts = 0
    correct = False
    while correct == False:
        guess = int(input("Enter your guess:/n"))
        attempts += 1
        if guess > target:
            print("Too high - try again:")
        elif guess < target:
            print("Too low - try again:")
        else:
            correct = True
    if attempts == 1:
        print("You guessed it in 1 try.")
    else:
        print(f"You guessed it in {attempts} tries.")
if __name__ == "__main__":
    guess()
