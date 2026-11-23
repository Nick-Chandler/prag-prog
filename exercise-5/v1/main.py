import turtle
import v1.utils
import v1.turtlelib
from collections.abc import Iterable


def execute_line(current_pen:turtle.Turtle, instruction: str) -> turtle.Turtle:
	command, arg = v1.utils.parse_line(instruction)
	current_pen = v1.turtlelib.instruction_table[command](current_pen, command, arg)
	return current_pen

def execute(commands:Iterable):
	current_pen = v1.turtlelib.PENS[0]
	for c in commands:
		current_pen = execute_line(current_pen, c)

if __name__ == "__main__":
	commands = ("P 2", "D", "W 2", "N 1", "E 2", "S 1", "U", "S 3","D","W 1", "N 1", "E 1", "S 1")
	execute(commands)
	turtle.done()