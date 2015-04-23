# Algorithm Tests

# Needed Python libraries
import csv
import sys
import random
from timeit import Timer
from multiprocessing import Process

# Import our algorithms
from algorithm1 import *
from algorithm2 import *
from algorithm3 import *
from algorithm4 import *

# Global Variables
max_time = 5*60 # 5 minutes
min_num = -99
max_num = 99

def run_test(Alg):
	f_name = "alg_res{0}.csv".format(Alg)
	with open(f_name, 'wb') as csvfile:
		writer = csv.writer(csvfile)

		for n in range(0, 1000000, 5):
			# build a random array of len n
			A = []
			for _ in range(n):
				A.append(random.randint(min_num, max_num))

			# determine which algorithm to call
			# run each set 3 times
			if Alg == 1:
				t = Timer(lambda: algorithm1(A)).timeit(number=3)
			elif Alg == 2:
				t = Timer(lambda: algorithm2(A)).timeit(number=3)
			elif Alg == 3:
				t = Timer(lambda: algorithm3(A)).timeit(number=3)
			elif Alg == 4:
				t = Timer(lambda: algorithm4(A)).timeit(number=3)

			writer.writerow([n, t])

			# see if we've gone beyond our max time.
			# if we have, break the loop
			if t >= max_time:
				break;

def random_tests():
	jobs = []
	for i in range(1,5):
		p = Process(target=run_test, args=(i,))
		jobs.append(p)
		p.start()

	for p in jobs:
		p.join()

if __name__ == "__main__":
	random_tests()