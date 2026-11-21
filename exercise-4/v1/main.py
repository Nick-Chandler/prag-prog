import turtle
p1 = turtle.Turtle()
p2 = turtle.Turtle()
p3 = turtle.Turtle()
PENS = (p1, p2, p3)
selected:turtle.Turtle = PENS[0]

def select_pen(n:int):
	selected = PENS[n] # Didn't realize until afterwards this didn't do anything

def parse_line(line:str) -> tuple:
	if len(line) == 1:
		command = line
		arg = None
	else:
		command,arg = line.split(" ")
	print(f"command: {command}")
	print(f"arg: {arg}")
	return (command, arg)

def execute_line(line:str):
	# parse
	command, arg = parse_line(line)
	
	if arg is None:
		commands[command]
	else:
		arg = int(arg)
		commands[command](arg)
	pass

def execute_lines(lines:list):
	for line in lines:
		execute_line(line)

def move_north(distance):
	selected.setheading(90)
	selected.forward(distance*50)
	
def move_south(distance):
	selected.setheading(270)
	selected.forward(distance*50)
	
def move_east(distance):
	selected.setheading(0)
	selected.forward(distance*50)
	
def move_west(distance):
	selected.setheading(180)
	selected.forward(distance*50)

def do_pen_dir():
	pass

commands = {
	"P": select_pen,
	"D": selected.pendown,
	"N": move_north,
	"S": move_south,
	"E": move_east,
	"W": move_west,
	"U": selected.penup
}

if __name__ == "__main__":
	# read in commands
	with open("commands.txt","r") as f:
		lines = f.read().splitlines()

	execute_lines(lines)
	turtle.done()

