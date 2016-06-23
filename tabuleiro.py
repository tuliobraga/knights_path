class Tabuleiro:

	N = 0
	size = 0
	casas = []

	def __init__(self, N):
		self.N = N
		self.size = N*N
		for i in xrange(0, self.size):
			self.casas.append(False)

	def indice(self, x,y):
		return x*self.N+y

	def visitado(self, x,y):
		return self.casas[self.indice(x,y)]

	def visitar(self, x,y):
		self.casas[self.indice(x,y)] = True

	def imprimir(self):
		line = 4*self.N*"_"
		for i in xrange(0, self.size):
			if i%self.N == 0:
				print line
				line = ("x" if self.casas[i] else "o")
			else:
				line += " | " + ("x" if self.casas[i]  else "o")

		print line