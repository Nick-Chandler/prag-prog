import turtle

SCALE = 50  # pixels per cm


class Drawing:
  def __init__(self, pens=3):
    self.pens = [turtle.Turtle() for _ in range(pens)]
    self.pen = self.pens[0]
    for p in self.pens:
      p.penup()

  def p(self, n):
    self.pen = self.pens[n - 1]

  def d(self):
    self.pen.pendown()

  def u(self):
    self.pen.penup()

  def n(self, dist):
    self._move(90, dist)

  def s(self, dist):
    self._move(270, dist)

  def e(self, dist):
    self._move(0, dist)

  def w(self, dist):
    self._move(180, dist)

  def _move(self, heading, dist):
    self.pen.setheading(heading)
    self.pen.forward(dist * SCALE)


if __name__ == "__main__":
  t = Drawing()
  t.p(2)  # select pen 2
  t.d()   # pen down
  t.w(2)  # draw west 2cm
  t.n(1)  # then north 1
  t.e(2)  # then east 2
  t.s(1)  # then back south
  t.u()   # pen up
  turtle.done()
