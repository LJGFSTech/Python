#Attribute and Methods in Python Turtle Graphics
#import/load turtle module
import turtle

#call the Turtle and Screen "types" in the turtle module and assign them to a variable.
#Note: Types are uppercase
t = turtle.Turtle()
wn = turtle.Screen()

#set turtle attributes
t.color("green")   # list of colors: http://www.tcl.tk/man/tcl8.4/TkCmd/colors.htm
t.pensize(7)
t.shape("turtle")  # "arrow" "blank" "circle" "classic" "square" "triangle" "turtle"  In shell type wn.getshapes() to get shape attributes
t.speed (1)        # speed can be set between 1 and 10

#set canvas attributes 
wn.bgcolor("skyblue") 
wn.title("Turtle Power!")

#turtle is placed on a coordinate plane. It starts at (0,0)
#move the turtle with the functions that it already knows (number of pixels)
# laura is an object and we can invoke methods/instructions


# DRAW a triangle with three different colored sides. Color name is a string
t.color("blue")
t.forward(200)
t.left(120)
t.color("green")
t.forward(200)
t.left(120)
t.color("hotpink")
t.forward(200)

#stamp leaves an impressions on the canvas

t.stamp()
t.penup()
t.forward(30)
t.stamp()
t.penup()
t.forward(30)
t.stamp()

# MAKE A SECOND TURTLE

#ends program when user to clicks on window
wn.exitonclick()

