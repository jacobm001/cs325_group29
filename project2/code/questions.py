import sys
from timeit import Timer
from project2_rbt import *
from multiprocessing import Process

def q4():
	f = open('../questions/q4.csv', 'w')
	f.write('A,changegreedy,changedp\n')

	V = [1,5,10,25,50]
	r = {}
	for A in range(2010, 2201, 5):
		r['g'] = changegreedy(V,A)[1]
		r['d'] = changedp(V,A)[1]

		f.write('{0},{1},{2}\n'.format(A, r['g'], r['d']))

	f.close()

def q5():
	f = open('../questions/q5.csv', 'w')
	f.write('A,changegreedy V1,changegreedy V2,changedp V1, changedp V2\n')

	V1 = [1,2,6,12,24,48,60]
	V2 = [1,6,13,37,150]
	r = {}
	for A in range(2000, 2201, 1):
		r['g1'] = changegreedy(V1, A)[1]
		r['g2'] = changegreedy(V2, A)[1]
		r['d1'] = changedp(V1, A)[1]
		r['d2'] = changedp(V2, A)[1]

		f.write('{0},{1},{2},{3},{4}\n'.format(A,r['g1'],r['g2'],r['d1'],r['d2']))

	f.close()

def q6():
	f = open('../questions/q6.csv', 'w')
	f.write('A,changegreedy,changedp\n')

	V = []
	V.append(1)
	for v in range(2, 31, 2):
		V.append(v)

	r = {}
	for A in range(2000, 2201, 5):
		r['g'] = changegreedy(V,A)[1]
		r['d'] = changedp(V,A)[1]

		f.write('{0},{1},{2}\n'.format(A, r['g'], r['d']))

	f.close()

def time_slow():
	f = open('../questions/time_slow.csv', 'w')
	f.write('A,Time\n')

	V = [1,5,10,25]
	for A in range(2, 100, 2):
		t = Timer(lambda: changeslow(V,A)).timeit(number=3)
		f.write('{0},{1}\n'.format(A,t))
		
		if t >= 20:
			break

	f.close()

def time_greedy():
	f = open('../questions/time_greedy.csv', 'w')
	f.write('A,Time\n')

	V = [1,5,10,25]
	for A in range(100, 1000001, 100):
		t = Timer(lambda: changegreedy(V,A)).timeit(number=3)
		f.write('{0},{1}\n'.format(A,t))
		
		if t >= 10:
			break

	f.close()

def time_dp():
	f = open('../questions/time_dp.csv', 'w')
	f.write('A,Time\n')

	V = [1,5,10,25]
	for A in range(100, 1000001, 1000):
		t = Timer(lambda: changedp(V,A)).timeit(number=3)
		f.write('{0},{1}\n'.format(A,t))
		
		if t >= 2:
			break

	f.close()

if __name__ == "__main__":
	print 'q4'
	q4()
	
	print 'q5'
	q5()
	
	print 'q6'
	q6()

	print 'slow'
	time_slow()
	
	print 'greedy'
	time_greedy()
	
	print 'dp'
	time_dp()