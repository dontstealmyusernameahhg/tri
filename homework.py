import turtle
turtle.Screen().bgcolor("white")
board = turtle.Turtle()
side_length = 100
for _ in range(4):
    board.forward(side_length)
    board.right(90)
turtle.done()