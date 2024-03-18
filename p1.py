import random

def guess_the_number():
    print("\n\nWelcome to the Guess the Number Game!\n\n")
    attempts = 0
    secret_num = random.randint(1, 100)
    user_guess = int(input("Enter your guess (between 1 and 100): "))
    
    
    k=int(input("Enter 0 to exit and 1 to stay : "))
    while (k!=0):
        attempts += 1
        if(user_guess==secret_num)and (user_guess<=100):
            print(f"Congratulations! You guessed the number {secret_number} in {attempts} attempts!\n\n")
            break
        elif(user_guess>100):
            print("You are guessing out of Range!!!")
        else:
            b=abs(user_guess - secret_num)
            print(f"You are {b} closer to the Secret Number")
            print("Try Again !!\n\n")
        secret_num = random.randint(1, 100)
        user_guess = int(input("Enter your guess (between 1 and 100): "))
        k=int(input("Enter 0 to exit and 1 to stay : "))
    print("EXITING.....")

guess_the_number()
