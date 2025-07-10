def check_age():
    try:
        age = int(input("Enter your age: "))
        if age < 0:
            print("Age cannot be negative.")
        else:
            if age % 2 == 0:
                print("You are an even-aged person.")
            else:
                print("You are an odd-aged person.")
    except ValueError:
        print("Invalid input. Please enter a valid integer for age.")