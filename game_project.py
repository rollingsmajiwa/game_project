print("Please select one level: 1. High 2. Medium 3. Low")
games = [1, 2, 3]
User_answer = int(input(":"))
if User_answer == games[0]:
        user_choice = int(input("Enter your selected number:"))
        real_answer = random.randint(1, 100)
        attempts = 0
        is_numrange = range(3)
        for i in is_numrange:
            if user_choice == real_answer:
                print("correct")
                break
            else:
                print("failed")
                attempts += 1
            user_choice = int(input("Try again:"))
            if attempts == 3:
                print(f"The answer is {real_answer}")
                break
    