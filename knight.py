from functions import index
import random

class Knight:

	max_moves = 8
	board = None

	def __init__(self, board):
		self.board = board

	# find out the available moves
	def availableMoves(self, current_x, current_y):
		# possible moves
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

		# check available moves
		availableMoves = []
		for x,y in moves:
			if x >= 0 and y >= 0 and x < self.board.N and y < self.board.N and not self.board.visited(x,y):
				availableMoves.append((x,y))

		return availableMoves

	# knight's path algorithm
	def knightsPath(self):
		# set a random initial position
		x=random.randint(0, self.board.N-1)
		y=random.randint(0, self.board.N-1)

		# initialize path as empty list
		path = []

		# goal function / evaluation function
		while len(path) < self.board.size:
			# make a move
			#print "move:",x,y
			self.board.visit(x,y)
			#self.board.show()
			path.append((x,y))

			# verify next available moves
			moves = self.availableMoves(x,y)
			num_moves = float("inf")
			for px,py in moves:
				next_moves = self.availableMoves(px,py)
				#print px, py, len(next_moves)
				# select the move with less next moves
				if len(next_moves) < num_moves:
					num_moves = len(next_moves)
					x = px
					y = py

		return len(set(path))
