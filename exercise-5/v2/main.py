import turtle

class Drawing:
	SCALE = 50
	COLORS = ("Black", "Blue", "Green")
	DIRECTIONS = {
		"E": 0,
		"N": 90,
		"W": 180,
		"S": 270
	}

	def __init__(self):
		self.color:str = "Black"
		self.pen = turtle.Turtle()

	def move(self, dir, dist):
		self.pen.setheading(self.DIRECTIONS[dir])
		self.pen.forward(dist*self.SCALE)

	def p(self, n):
		self.color = self.COLORS[n-1]
		
	def u(self):
		self.pen.penup()
		
	def d(self):
		self.pen.pendown()
		
	def e(self, dist):
		self.move("E",dist)
		
	def n(self, dist):
		self.move("N",dist)
		
	def w(self, dist):
		self.move("W",dist)
		
	def s(self, dist):
		self.move("S",dist)
		


if __name__ == "__main__":
	t = Drawing()
	t.p(2)
	t.d() 
	t.w(2) 
	t.n(1)
	t.e(2)
	t.s(1)  
	t.u()   
	turtle.done()