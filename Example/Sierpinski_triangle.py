import turtle
from Lsystemscript import lsystem
bob = turtle.Turtle()
bob.left(90)
input = lsystem(2)
for i in input:
    if(i == 'F') or (i =='G'):
        bob.forward(40)
    elif(i == '+'):
        bob.left(120)
    elif(i == '-'):
        bob.right(120)
turtle.done()
