import random

def get_positive_number():
    while True:
        try:
            number = int(input("Enter a positive number: "))
            if number <= 0:
                print("Please enter a positive number.")
            else:
                return number
        except ValueError:
            print("Please enter a valid positive number.")

def main():
    upper_limit = get_positive_number()
    target_number = random.randint(0, upper_limit)

    while True:
        try:
            guess = int(input(f"Guess the number between 0 and {upper_limit}: "))
            if guess > target_number:
                print("Too large!")
            elif guess < target_number:
                print("Too small!")
            else:
                print("Just right!")
                break
        except ValueError:
            print("Please enter a valid number for guessing.")

    print("Congratulations! You guessed the number.")

if __name__ == "__main__":
    main()
