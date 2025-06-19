char = input("Enter a character: ")
if len(char) != 1:
    print("Please enter a single character.")
else:
    if char.isalpha():
        print(f"The character '{char}' is an alphabet.")