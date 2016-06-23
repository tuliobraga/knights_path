from functions import index

class Knight:

	max_moves = 8
	board = None

	def __init__(self, board):
		self.board = board

	# find out the available moves
	def availableMoves(self, current_x, current_y):
		x_p2 = current_x + 2
		x_p1 = current_x + 1
		x_m2 = current_x - 2
		x_m1 = current_x - 2
		y_p2 = current_y + 2
		y_p1 = current_y + 1
		y_m2 = current_y - 2
		y_m1 = current_y - 1

		moves = [
			(x_p2, y_p1),
			(x_p2, y_m1),
			(x_m2, y_p1),
			(x_m2, y_m1),
			(x_p1, y_p2),
			(x_p1, y_m2),
			(x_m1, y_p2),
			(x_m1, y_m2),
		]

		availableMoves = []
		for x,y in moves:
			if x >= 0 and y >= 0:
				availableMoves.append((x,y))

		return availableMoves

	# knight's path algorithm
	def knightsPath(self):
		# init knights at 0,0 board coordinate
		self.board.visit(0,0)

		# print board's initial state
		self.board.show()
		moves = self.availableMoves(0,0)
		x,y = moves.pop();

		squares_visited = 1
		while squares_visited < self.board.size:
			if not self.board.visited(x,y):
				self.board.visit(x,y)
				self.board.show()
				squares_visited+=1

