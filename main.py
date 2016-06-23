import sys
from tabuleiro import Tabuleiro

if len(sys.argv) < 2:
	print "Tamanho tabuleiro nao foi definido. Use 'python main.py [tamanho]'"
	sys.exit()
# tamanho do tabuleiro
N = int(sys.argv[1])

tabuleiro = Tabuleiro(N)
tabuleiro.imprimir()
tabuleiro.visitar(2,2)
tabuleiro.imprimir()