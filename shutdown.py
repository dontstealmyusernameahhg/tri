def shut_down():
    user_input = input("Do you want to shut down the computer? (yes/no): ")
    if user_input == "yes":
        print("Shutting down...")
    elif user_input == "no":
        print("Abort shut down")
    else:
        print("Sorry")
shut_down()