import turtle

p1 = turtle.Turtle()
p2 = turtle.Turtle()
p3 = turtle.Turtle()

PENS = (p1,p2,p3)

def move(pen: turtle.Turtle, direction:str, distance:int):
	headings = {
		"E": 0,
		"N": 90,
		"W": 180,
		"S": 270
	}

	pen.setheading(headings[direction])
	pen.forward(distance*50)
	return pen

def penup(pen:turtle.Turtle, command:str, arg:int):
	pen.penup()
	return pen

def pendown(pen: turtle.Turtle, command:str, arg:int):
	pen.pendown()
	return pen

def select_pen(pen:turtle.Turtle, command:str, new_pen:int):
	return PENS[new_pen-1]
	
instruction_table = {
	"N": move,
	"S": move,
	"E": move,
	"W": move,
	"U": penup,
	"D": pendown,
	"P": select_pen
}