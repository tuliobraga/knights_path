import sys
from knight import Knight
from board import Board

if len(sys.argv) < 2:
	print "Board size is not defined. Use 'python main.py [tamanho]'"
	sys.exit()

# board size
N = int(sys.argv[1])

b = Board(N)
k = Knight(b)
k.knightsPath()