from cell import Cell

import random
import time

class Maze:

	def __init__(self, margin_x, margin_y, num_rows, num_cols, cell_size_x, cell_size_y, win=None, seed=None):

		self._cells = []
		self._margin_x = margin_x
		self._margin_y = margin_y
		self._num_rows = num_rows
		self._num_cols = num_cols
		self._cell_size_x = cell_size_x
		self._cell_size_y = cell_size_y
		self._win = win

		if seed:
			random.seed(seed)

		self._create_cells()
		self._break_walls(0, 0)
		self._reset_visited_cells()

	def _create_cells(self):
		for i in range(0, self._num_cols):
			column = []
			for j in range(0, self._num_rows):
				column.append(Cell(self._win))
			self._cells.append(column)

		self._break_entrance_and_exit()

		for i in range(0, self._num_cols):
			for j in range(0, self._num_rows):
				self._draw_cell(i, j)

	def _draw_cell(self, i, j):
		if self._win is None:
			return
		x1 = self._margin_x + (i * self._cell_size_x)
		y1 = self._margin_y + (j * self._cell_size_y)
		x2 = x1 + self._cell_size_x
		y2 = y1 + self._cell_size_y
		self._cells[i][j].draw(x1, y1, x2, y2)
		self._animate()
	
	def _animate(self):
		if self._win is None:
			return
		self._win.redraw()
		time.sleep(0.01)

	def _reset_visited_cells(self):
		for column in self._cells:
			for cell in column:
				cell.visited = False

	def _break_entrance_and_exit(self):
		
		entrance = self._cells[0][0]
		entrance.has_top_wall = False
		
		exit = self._cells[self._num_cols - 1][self._num_rows - 1]
		exit.has_bottom_wall = False
	
	def _break_walls(self, i, j):
		self._cells[i][j].visited = True
		while True:
			targets = []
			# Check left cell
			if i > 0 and not self._cells[i - 1][j].visited:
				targets.append((i - 1, j))
			# Check right cell
			if i < (self._num_cols - 1) and not self._cells[i + 1][j].visited:
				targets.append((i + 1, j))
			# Check cell above
			if j > 0 and not self._cells[i][j - 1].visited:
				targets.append((i, j - 1))
			# Check cell below
			if j < (self._num_rows - 1) and not self._cells[i][j + 1].visited:
				targets.append((i, j + 1))
			
			if len(targets) == 0:
				self._draw_cell(i, j)
				return
			
			direction = random.randrange(len(targets))
			target = targets[direction]

			if target[0] == i - 1:
				self._cells[i][j].has_left_wall = False
				self._cells[i - 1][j].has_right_wall = False
			if target[0] == i + 1:
				self._cells[i][j].has_right_wall = False
				self._cells[i + 1][j].has_left_wall = False
			if target[1] == j - 1:
				self._cells[i][j].has_top_wall = False
				self._cells[i][j - 1].has_bottom_wall = False
			if target[1] == j + 1:
				self._cells[i][j].has_bottom_wall = False
				self._cells[i][j + 1].has_top_wall = False

			self._break_walls(target[0], target[1])

	def _solve(self, i, j):
		self._animate()

		cell = self._cells[i][j]
		cell.visited = True

		# Check if we've reached the end
		if i == self._num_cols - 1 and j == self._num_rows - 1:
			return True
		
		if i > 0 and not cell.has_left_wall and not self._cells[i - 1][j].visited:
			cell.draw_move(self._cells[i - 1][j])
			if self._solve(i - 1, j):
				return True
			cell.draw_move(self._cells[i - 1][j], True)
		# Check right cell
		if i < (self._num_cols - 1) and not cell.has_right_wall and not self._cells[i + 1][j].visited:
			cell.draw_move(self._cells[i + 1][j])
			if self._solve(i + 1, j):
				return True
			cell.draw_move(self._cells[i + 1][j], True)
		# Check cell above
		if j > 0 and not cell.has_top_wall and not self._cells[i][j - 1].visited:
			cell.draw_move(self._cells[i][j - 1])
			if self._solve(i, j - 1):
				return True
			cell.draw_move(self._cells[i][j - 1], True)
		# Check cell below
		if j < (self._num_rows - 1) and not cell.has_bottom_wall and not self._cells[i][j + 1].visited:
			cell.draw_move(self._cells[i][j + 1])
			if self._solve(i, j + 1):
				return True
			cell.draw_move(self._cells[i][j + 1], True)

		return False