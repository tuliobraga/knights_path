from functions import index

class Knight:

	board = None

	def __init__(self, board):
		self.board = board

	def knightsPath(self):
		self.board.show()
		self.board.visit(2,2)
		self.board.show()