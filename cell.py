from constants import *
from graphics import Line, Point

class Cell:
	def __init__(self, win=None):
		self._window = win
		self.visited = False
		self.has_left_wall = True
		self.has_right_wall = True
		self.has_top_wall = True
		self.has_bottom_wall = True
		self._x1 = None
		self._y1 = None
		self._x2 = None
		self._y2 = None
	def draw(self, x1, y1, x2, y2):
		if self._window is None:
			return
		self._x1 = x1
		self._y1 = y1
		self._x2 = x2
		self._y2 = y2
		# Left wall
		line = Line(Point(x1, y1), Point(x1, y2))
		if self.has_left_wall:
			self._window.draw_line(line, WALL_COLOUR)
		else:
			self.erase_line(line)
		# Right wall
		line = Line(Point(x2, y2), Point(x2, y1))
		if self.has_right_wall:
			self._window.draw_line(line, WALL_COLOUR)
		else:
			self.erase_line(line)
		# Top wall
		line = Line(Point(x1, y1), Point(x2, y1))
		if self.has_top_wall:
			self._window.draw_line(line, WALL_COLOUR)
		else:
			self.erase_line(line)
		# Bottom wall
		line = Line(Point(x1, y2), Point(x2, y2))
		if self.has_bottom_wall:
			self._window.draw_line(line, WALL_COLOUR)
		else:
			self.erase_line(line)
	def draw_move(self, to_cell, undo=False):
		colour = PATH_COLOUR if not undo else DEAD_END_COLOUR
		p1 = Point((self._x1 + self._x2) / 2, (self._y1 + self._y2) / 2)
		p2 = Point((to_cell._x1 + to_cell._x2) / 2, (to_cell._y1 + to_cell._y2) / 2)
		line = Line(p1, p2)
		self._window.draw_line(line, colour)
	def erase_line(self, line):
		red_start, green_start, blue_start = self._window._get_color_info(BACKGROUND_GRADIENT_START)
		red_end, green_end, blue_end = self._window._get_color_info(BACKGROUND_GRADIENT_END)
		y = (line.p1.y + line.p2.y) // 2
		red = red_start + int(y * (red_end - red_start) // self._window._height)
		green = green_start + int(y * (green_end - green_start) // self._window._height)
		blue = blue_start + int(y * (blue_end - blue_start) // self._window._height)
		color = "#%04x%04x%04x" % (red, green, blue)
		if line.p1.x == line.p2.x and line.p1.y < line.p2.y:
			line.p1.y += 1
			line.p2.y -= 1
		if line.p1.x == line.p2.x and line.p1.y > line.p2.y:
			line.p1.y -= 1
			line.p2.y += 1
		if line.p1.y == line.p2.y and line.p1.x < line.p2.x:
			line.p1.x += 1
			line.p2.x -= 1
		if line.p1.y == line.p2.y and line.p1.x > line.p2.x:
			line.p1.x -= 1
			line.p2.x += 1
		self._window.draw_line(line, color)
