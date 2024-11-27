from graphics import Line, Point

class Cell:
	def __init__(self, win):
		self._window = win
		self._x1 = None
		self._y1 = None
		self._x2 = None
		self._y2 = None
		self.has_left_wall = True
		self.has_right_wall = True
		self.has_top_wall = True
		self.has_bottom_wall = True
	def draw(self, x1, y1, x2, y2):
		if self._window is None:
			return
		self._x1 = x1
		self._y1 = y1
		self._x2 = x2
		self._y2 = y2
		if self.has_left_wall:
			line = Line(Point(x1, y1), Point(x1, y2))
			self._window.draw_line(line, "darkblue")
		if self.has_right_wall:
			line = Line(Point(x2, y2), Point(x2, y1))
			self._window.draw_line(line, "darkblue")
		if self.has_top_wall:
			line = Line(Point(x1, y1), Point(x2, y1))
			self._window.draw_line(line, "darkblue")
		if self.has_bottom_wall:
			line = Line(Point(x1, y2), Point(x2, y2))
			self._window.draw_line(line, "darkblue")
	def draw_move(self, to_cell, undo=False):
		colour = "red" if not undo else "grey"
		p1 = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
		p2 = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)
		line = Line(p1, p2)
		self._window.draw_line(line, colour)