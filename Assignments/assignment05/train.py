#By Elizabeth Hall


import turtle

turtle.bgcolor("skyblue")
turtle.setup(500,500)
pen = turtle.Turtle()
pen.pensize(2)
pen.speed(.5)
pen.color("black")
pen.fillcolor("red")

#Train Width
trainWidth = float(input("How large on a scale of 100 to 200 would you like to draw your train?: "))
trainBoxWidth = trainWidth * 2/4
trainCabWidth = trainWidth - trainBoxWidth

#Train Heights
trainHeight = trainWidth * 7/8
trainBoxHeight = trainHeight * 2/3
trainCabHeight = trainBoxHeight * 2/3
trainWheelRadius = (trainHeight - trainBoxHeight)/2

#Train Frame
pen.up()
pen.setpos(-trainWidth/2,-trainHeight/2 + trainWheelRadius *2)
pen.down()
pen.begin_fill()
pen.forward(trainWidth)
pen.left(90)
pen.forward(trainCabHeight)
pen.left(90)
pen.forward(trainCabWidth)
pen.right(90)
pen.forward(trainBoxHeight - trainCabHeight)
pen.left(90)
pen.forward(trainBoxWidth)
pen.left(90)
pen.forward(trainBoxHeight)
pen.end_fill()

#Roof
pen.up()
pen.setpos(-trainWidth * 3/5, trainBoxHeight *2.25)
pen.begin_fill()
pen.color("red")
pen.forward(trainHeight)
pen.left(90)
pen.forward(trainBoxWidth * 1.3)
pen.left(90)
pen.forward(trainCabHeight/2)
pen.left(90)
pen.forward(trainBoxWidth * 1.3)
pen.left(90)
pen.forward(trainHeight/3)
pen.end_fill()

#Window
pen.up()
pen.setpos(-trainWidth * 2/5, trainBoxHeight * 2.15)
pen.fillcolor("skyblue")
pen.color("skyblue")
pen.down()
pen.forward(trainHeight * 1.25)
pen.left(90)
pen.forward(trainBoxWidth/1.60)
pen.left(90)
pen.forward(trainCabHeight/2)
pen.left(90)
pen.forward(trainBoxWidth/1.60)
pen.left(90)
pen.forward(trainHeight * 1.25)
pen.end_fill()

#Wheels
pen.up()
pen.setpos(-trainWidth/2.25 + trainWidth * 1/3 - trainWheelRadius, -trainHeight/2.5 + trainWheelRadius)
pen.down()
pen.fillcolor("black")
pen.color("black")
pen.begin_fill()
pen.circle(trainWheelRadius)
pen.end_fill()

pen.up()
pen.setpos(-trainWidth/1.25 + trainWidth * 1/3 - trainWheelRadius, -trainHeight/2.5 + trainWheelRadius)
pen.down()
pen.fillcolor("black")
pen.color("black")
pen.begin_fill()
pen.circle(trainWheelRadius)
pen.end_fill()

pen.up()
pen.setpos(-trainWidth + trainWidth * 1.3 - trainWheelRadius, -trainHeight/2.5 + trainWheelRadius)
pen.down()
pen.fillcolor("black")
pen.color("black")
pen.begin_fill()
pen.circle(trainWheelRadius/2)
pen.end_fill()

pen.up()
pen.setpos(-trainWidth + trainWidth * 1.5 - trainWheelRadius, -trainHeight/2.5 + trainWheelRadius)
pen.down()
pen.fillcolor("black")
pen.color("black")
pen.begin_fill()
pen.circle(trainWheelRadius/2)
pen.end_fill()




turtle.done()


