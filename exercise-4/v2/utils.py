import pathlib
from collections import deque

def read_instructions(path:pathlib.Path) -> deque:
	with path.open("r") as f:
		str_lines = f.read().splitlines()
		instructions_queue = deque(str_lines)
	return instructions_queue

# store command, arg
def parse_instruction(instruction: str) -> tuple[str, int | None]:
	split = instruction.split(" ")
	command = split[0]
	if len(split) == 1:
		arg = None
	else:
		arg = int(split[1])
	return (command, arg)


	
	