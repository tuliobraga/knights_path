import sys
from knight import Knight
from board import Board
from datetime import datetime
from math import sqrt

if len(sys.argv) < 2:
	print "Board size is not defined. Use 'python main.py [tamanho]'"
	sys.exit()

# board size
#N = int(sys.argv[1])


sizes = [5, 8, 16, 32, 64, 128, 256, 512, 1024]
for N in sizes:
	print "#############"
	print "%d=%d" % (N, N*N)
	print "#############"
	results = []
	sum_time2 = 0.0
	sum_time = 0.0
	for i in xrange(0, 30):

		#start = current_milli_time()
		# knights tour
		b = Board(N)
		k = Knight(b)
		r = k.knightsPath()
		#end = current_milli_time()
		#t = end-start

		#sum_time2 += t*t
		#sum_time += t
		results.append(r);

	#variance = (sum_time2 - (sum_time*sum_time)/30)/30-1;
	#standardDeviation = sqrt(variance);
	#print "Total time: %fms / Average time: %fms / Standard Deviation: %fms" % (sum_time,sum_time/30.0,standardDeviation)
	print results