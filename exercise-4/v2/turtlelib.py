import turtle

p1 = turtle.Turtle() 
p2 = turtle.Turtle() 
p3 = turtle.Turtle() 

PENS = (p1,p2,p3)

def pendown(pen:turtle.Turtle,command:str,arg:int):
	pen.pendown()
	return pen
	
def penup(pen:turtle.Turtle,command:str,arg:int):
	pen.penup()
	return pen

def do_pen_dir(pen:turtle.Turtle, direction:str, distance: int):
	headings = {
		"E": 0,
		"N": 90,
		"W": 180,
		"S": 270
	}
			
	pen.setheading(headings[direction])
	pen.forward(distance*50)
	return pen
	
