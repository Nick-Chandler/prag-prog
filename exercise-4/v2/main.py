import pathlib
import turtle

import turtlelib
import utils

def select_pen(old_pen:turtle.Turtle, command:str, new_pen:int):
	selected = turtlelib.PENS[new_pen-1]
	return selected
	
instruction_table = {
	"U": turtlelib.penup,
	"D": turtlelib.pendown,
	"P": select_pen,
	"N": turtlelib.do_pen_dir,
	"S": turtlelib.do_pen_dir,
	"E": turtlelib.do_pen_dir,
	"W": turtlelib.do_pen_dir
}



def execute_line(instruction: str, current_pen:turtle.Turtle) -> turtle.Turtle:
	command, arg = utils.parse_instruction(instruction)
	func = instruction_table[command]

	current_pen = func(current_pen,command,arg)
	return current_pen
	
		

def execute(path:pathlib.Path, selected: turtle.Turtle):
	instructions = utils.read_instructions(path)
	while instructions:
		todo = instructions.popleft()
		selected = execute_line(todo, selected)

if __name__ == "__main__":
	path = pathlib.Path("commands.txt")
	selected = turtlelib.PENS[0]
	execute(path,selected)
	turtle.done()
	
	