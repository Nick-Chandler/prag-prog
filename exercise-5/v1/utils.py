def parse_line(instruction: str) -> tuple[str,int | None]:
	split = instruction.split(" ")
	command:str = split[0]
	if len(split) == 1:
		return (command, None)
	arg: int = int(split[1])
	return (command, arg)