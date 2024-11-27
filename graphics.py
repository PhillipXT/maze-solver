from constants import *
from tkinter import Tk, BOTH, Canvas

class Point:
	def __init__(self, x, y):
		self.x = x
		self.y = y

class Line:
	def __init__(self, p1, p2):
		self.p1 = p1
		self.p2 = p2
	def draw(self, canvas, fill_colour=WALL_COLOUR):
		canvas.create_line(self.p1.x, self.p1.y, self.p2.x, self.p2.y, fill=fill_colour, width=3)

class Window:
	def __init__(self, width, height):
		self._height = height
		self._width = width
		self.__root = Tk()
		self.__root.title("Maze Solver")
		self.__root.protocol("WM_DELETE_WINDOW", self.close)
		self.__canvas = Canvas(self.__root, bg=BACKGROUND_COLOUR, height=height, width=width)
		self.__canvas.pack(fill=BOTH, expand=1)
		self.__running = False
		self._draw_gradient()
	def _get_color_info(self, color):
		return self.__root.winfo_rgb(color)
	def _draw_gradient(self):
		red_start, green_start, blue_start = self.__root.winfo_rgb(BACKGROUND_GRADIENT_START)
		red_end, green_end, blue_end = self.__root.winfo_rgb(BACKGROUND_GRADIENT_END)
		for i in range(self._height):
			red = red_start + (i * (red_end - red_start) // self._height)
			green = green_start + (i * (green_end - green_start) // self._height)
			blue = blue_start + (i * (blue_end - blue_start) // self._height)
			color = "#%04x%04x%04x" % (red, green, blue)
			self.__canvas.create_line(0, i, self._width, i, fill=color)
	def redraw(self):
		self.__root.update_idletasks()
		self.__root.update()
	def wait_for_close(self):
		self.__running = True
		while self.__running:
			self.redraw()
	def draw_line(self, line, fill_colour=WALL_COLOUR):
		line.draw(self.__canvas, fill_colour)
	def close(self):
		self.__running = False
