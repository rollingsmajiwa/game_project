import random

print("Please select one level: 1. Hard 2. Medium 3. Low")
games = [1, 2, 3]
attempts = 0
User_answer = int(input(":"))
if User_answer == games[0]:
        user_choice = int(input("Enter your selected number(1 - 100):"))
        real_answer = random.randint(1, 100)
        maximum_attempt = 5
        is_numrange = range(5)
        for i in is_numrange:
            if user_choice == real_answer:
                print("correct")
                break
            else:
                if user_choice > real_answer:
                    print("Your guess is Too high")
                else:
                    print("Your guesss is Too low")
                Remaining_attempts = maximum_attempt - attempts
                print(f"Remaining attempts are {Remaining_attempts}. Try again")
                attempts += 1
            user_choice = int(input("Try again:"))
            if attempts == 5:
                print(f"The answer is {real_answer}")
                break
elif User_answer == games[1]:
    user_choice = int(input("Enter your selected number(1 -100):"))
    real_answer = random.randint(1, 100)
    is_numrange = range(7)
    maximum_attempt = 7
    for i in is_numrange:
        if user_choice == real_answer:
            print("correct")
            break
        else:
            if user_choice > real_answer:
                print(" Your guess is Too high")
            else:
                print(" Your guess is Too low")
            Remaining_attempts = maximum_attempt - attempts
            print(f"Remaining attempts are {Remaining_attempts}. Try again")
            attempts += 1
            user_choice = int(input("Try again:"))
            if attempts == 7:
                print(f"The answer is {real_answer}")
                break
elif User_answer == games[2]:
    user_choice = int(input("Enter your selected number(1-100):"))
    real_answer = random.randint(1, 100)
    maximum_attempt = 10
    is_numrange = range(10)
    for i in is_numrange:
        if user_choice == real_answer:
            print("correct")
            break
        else:
            if user_choice > real_answer:
                print("Your guess is Too high")
            else:
                print("Your guess is Too low")
            Remaining_attempts = maximum_attempt - attempts
            print(f"Remaining attempts are {Remaining_attempts}. Try again")
            attempts += 1
            user_choice = int(input("Try again:"))
            if attempts == 10:
                print(f"The answer is {real_answer}")
                break   