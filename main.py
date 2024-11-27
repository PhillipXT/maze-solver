from graphics import Window
from cell import Cell

def main():
	win = Window(800, 600)

	cell1 = Cell(win)
	cell1.has_bottom_wall = False
	cell1.draw(100, 100, 150, 150)

	cell2 = Cell(win)
	cell2.has_left_wall = False
	cell2.has_right_wall = False
	cell2.draw(200, 200, 250, 250)

	cell3 = Cell(win)
	cell3.has_top_wall = False
	cell3.draw(300, 300, 350, 350)
	cell3.draw_move(cell2)

	win.wait_for_close()

main()