#Author Elizabeth Hall

import turtle

turtle.bgcolor("grey")

pen = turtle.Turtle()

pen.pensize(10)

#draw a pumpkin
pen.setposition(-50,50)
pen.begin_fill()
pen.color("orange")
pen.fillcolor("orange")
pen.forward(100)
pen.right(60)
pen.forward(100)
pen.right(60)
pen.forward(100)
pen.right(60)
pen.forward(100)
pen.right(60)
pen.forward(100)
pen.right(60)
pen.forward(100)
pen.end_fill()
pen.up()

#pumpkin stem
pen.setposition(-5,50)
pen.begin_fill()
pen.color("green")
pen.fillcolor("green")
pen.down()
pen.forward(50)
pen.right(175)
pen.forward(50)
pen.end_fill()
pen.up()

#pumpkin eye1
pen.setposition(-30,15)
pen.begin_fill()
pen.color("black")
pen.fillcolor("black")
pen.down()
pen.forward(30)
pen.left(120)
pen.forward(30)
pen.left(120)
pen.forward(30)
pen.end_fill()
pen.up()

#pumpkin eye2
pen.setposition(40,-5)
pen.begin_fill()
pen.color("black")
pen.fillcolor("black")
pen.down()
pen.forward(30)
pen.left(120)
pen.forward(30)
pen.left(120)
pen.forward(30)
pen.end_fill()
pen.up()

#pumpkin mouth
pen.setposition(-50,-75)
pen.begin_fill()
pen.color("black")
pen.fillcolor("black")
pen.down()
pen.forward(20)
pen.right(60)
pen.forward(20)
pen.left(60)
pen.forward(20)
pen.right(10)
pen.forward(20)
pen.left(60)
pen.forward(20)
pen.right(0)
pen.forward(20)
pen.left(210)
pen.forward(20)
pen.left(300)
pen.forward(20)
pen.left(320)
pen.forward(20)
pen.left(60)
pen.forward(30)
pen.left(250)
pen.forward(30)
pen.left(200)
pen.forward(25)
pen.right(185)
pen.forward(20)
pen.right(200)
pen.forward(25)
pen.end_fill()
pen.up()


#moon had some help from pythonturtle.academy
pen.setposition(100,75)
pen.begin_fill()
pen.color("yellow")
pen.fillcolor("yellow")
pen.down()
pen.circle(75)
pen.end_fill()

pen.setposition(150,75)
pen.begin_fill()
pen.color("grey")
pen.fillcolor("grey")

pen.circle(75)
pen.end_fill()



turtle.done()