#Introduction to Python Turtle Graphics
#import/load turtle module
import turtle

#call the Turtle and Screen "types" in the turtle module and assign them to a variable.
#Note: Types are uppercase
t = turtle.Turtle()
wn = turtle.Screen()

#turtle is placed on a coordinate plane. It starts at (0,0) and facing right
#move the turtle with the functions that it already knows (number of pixels)
# laura is an object and we can invoke methods/instructions

# DRAW A SQURE 

t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)
t.left(90)
t.forward(100)

# pen control

# DRAW A DASHED LINE
t.penup()
t.forward(50)
t.pendown()
t.forward(50)

t.penup()
t.forward(50)
t.pendown()
t.forward(50)

#absolute motion (not relative motion)
t.goto(0,0)
t.goto(300,0)
t.goto(-300,0)


#ends program when user to clicks on window
wn.exitonclick()


