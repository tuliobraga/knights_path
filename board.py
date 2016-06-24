from functions import index

class Board:

	N = 0
	size = 0
	squares = []

	def __init__(self, N):
		self.N = N
		self.size = N*N
		self.squares = []
		for i in xrange(0, self.size):
			self.squares.append(False)

	# verify if square is already visited
	def visited(self,x,y):
		return self.squares[index(x,y,self.N)]

	# visit a square
	def visit(self, x,y):
		self.squares[index(x,y,self.N)] = True

	# print board
	def show(self):
		line = 4*self.N*"_"
		for i in xrange(0, self.size):
			if i%self.N == 0:
				print line
				line = ("x" if self.squares[i] else "o")
			else:
				line += " | " + ("x" if self.squares[i]  else "o")

		print line