import turtle 
turtle.Screen().bgcolor("light blue")
sc=turtle.Screen()
sc.setup(800,600) 
turtle.title("welcome to my turtle window")
board=turtle.Turtle()
for i in range(4):
    board.forward(100)
    board.right(90)
    i+=1   
turtle.done()

