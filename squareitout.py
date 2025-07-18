def function(start, end):
    square_values = [i ** 2 for i in range(start, end + 1)]
    even_squares = [value for value in square_values if value % 2 == 0]
    odd_squares = [value for value in square_values if value % 2 != 0]
    print("square values:", square_values)
    print("even square values:", even_squares)
    print("odd square values:", odd_squares)
start = int(input("Enter the start value: "))
end = int(input("Enter the end value: "))
function(start, end)
# squareitout.py
# This script calculates the square of numbers in a given range and categorizes them into even and