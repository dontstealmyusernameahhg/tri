class Reverser:
    def reverse(self, s):
        return s[::-1]

# Example usage
if __name__ == "__main__":
    r = Reverser()
    input_string = input("Enter a string to reverse: ")
    reversed_string = r.reverse(input_string)
    print("Reversed string:", reversed_string)