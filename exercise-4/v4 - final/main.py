import pathlib
import turtle

colors = ("Black","Blue","Green")

pen = turtle.Turtle()

instructions = {
		"P": (True, lambda n: pen.pencolor(colors[n-1])),
		"U": (False, lambda: pen.penup()),
		"D": (False, lambda: pen.pendown()),
		"E": (True, lambda dist: move(pen,"E",dist)),
		"N": (True, lambda dist: move(pen,"N",dist)),
		"W": (True, lambda dist: move(pen,"W",dist)),
		"S": (True, lambda dist: move(pen,"S",dist)),
	}

def move(pen:turtle.Turtle, dir:str, dist:int):
	directions = {
		"E": 0,
		"N": 90,
		"W": 180,
		"S": 270,
	}

	heading = directions[dir]
	pen.setheading(heading)
	pen.forward(dist*50)

	
def execute(program:str) -> None:
	
	lines = program.splitlines()
	for line in lines:
		if not line:
			continue
			
		parts = line.split()

		command = parts[0]
		instruction = instructions[command]
		
		requires_arg = instruction[0]
		handler = instruction[1]

		if requires_arg:
			arg = int(parts[1])
			handler(arg)

		else: 
			handler()

	return

if __name__ == "__main__":
	program = pathlib.Path("commands.txt").read_text()
	execute(program)
	turtle.done()