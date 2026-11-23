import turtle

pen = turtle.Turtle()

def move(direction, distance):
  headings = {
    "N": 90,
    "E": 0,
    "S": 270,
    "W": 180
  }

  pen.setheading(headings[direction])
  pen.forward(distance * 100)


def parse(program:str):
  commands = {
    "P": (True, lambda n: pen.pencolor(["black", "red", "blue"][n])),
    "U": (False, pen.penup),
    "D": (False, pen.pendown),
    "N": (True, lambda n: move("N", n)),
    "E": (True, lambda n: move("E", n)),
    "S": (True, lambda n: move("S", n)),
    "W": (True, lambda n: move("W", n))
  }

  for line in program.splitlines():
    line = line.split("#")[0].strip()

    if not line:
      continue

    parts = line.split()
    command = parts[0]

    requires_arg, handler = commands[command]

    if requires_arg:
      handler(int(parts[1]))
    else:
      handler()


program = """
P 2
D
W 2
N 1
E 2
S 1
U
"""

pen.penup()
pen.goto(100, -50)

parse(program)

turtle.done()