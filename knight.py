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
		x_m1 = current_x - 1
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
			if x >= 0 and y >= 0 and x < self.board.N and y < self.board.N:
				availableMoves.append((x,y))

		return availableMoves

	# knight's path algorithm
	def knightsPath(self):
		# set initial position
		x=0
		y=0

		# initialize path as empty list
		path = []

		# goal function
		while len(path) < self.board.size:
			print "move:",x,y
			self.board.visit(x,y)
			self.board.show()
			path.append((x,y))
			moves = self.availableMoves(x,y)
			num_moves = float("inf")
			for px,py in moves:
				next_moves = self.availableMoves(px,py)
				print px, py, len(next_moves)
				if len(next_moves) < num_moves and not self.board.visited(px,py):
					num_moves = len(next_moves)
					x = px
					y = py

		print path
		print len(path)
