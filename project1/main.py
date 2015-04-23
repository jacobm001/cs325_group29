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

def print_fail(alg, a):
	print "Algorithm {0} failed with test {1}".format(alg, a)

def validate_algorithms():
	a = {}
	a["a1"] = [1, 4, -9, 8, 1, 3, 3, 1, -1, -4, -6, 2, 8, 19, -10, -11]
	a["a1_sub"] = [8, 1, 3, 3, 1, -1, -4, -6, 2, 8, 19]
	a["a1_ans"] = 34

	a["a2"] = [2, 9, 8, 6, 5, -11, 9, -11, 7, 5, -1, -8, -3, 7 -2]
	a["a2_sub"] = [2, 9, 8, 6, 5]
	a["a2_ans"] = 30

	a["a3"] = [10, -11, -1, -9, 33, -45, 23, 24, -1, -7 -8, 19]
	a["a3_sub"] = [23,24, -1, -7, -8, 19]
	a["a3_ans"] = 50

	a["a4"] = [31,-41, 59, 26, -53, 58, 97, -93, -23, 84]
	a["a4_sub"] = [59, 26, -53, 58, 97]
	a["a4_ans"] = 187

	a["a5"] = [3, 2, 1, 1, -8, 1, 1, 2, 3]
	a["a5_sub"] = [3, 2, 1, 1]
	a["a5_ans"] = 7

	for i in range(1,6):
		if sum(algorithm1(a["a{0}".format(i)])) != a["a{0}_ans".format(i)]:
			print_fail(1, i)
		if sum(algorithm2(a["a{0}".format(i)])) != a["a{0}_ans".format(i)]:
			print_fail(2, i)
		if sum(algorithm3(a["a{0}".format(i)])) != a["a{0}_ans".format(i)]:
			print_fail(3, i)
		if sum(algorithm4(a["a{0}".format(i)])) != a["a{0}_ans".format(i)]:
			print_fail(1, i)

def MSS_test():
	print "MSS_Test stuff goes here"

def print_help():
	print "Program argument error!"
	print "  Valid arguments include time_test, alg_test, or MSS_test"
	return None

if __name__ == "__main__":
	if len(sys.argv) < 2 :
		print_help()

	if sys.argv[1] == "time_test":
		random_tests()
	elif sys.argv[1] == "alg_test":
		validate_algorithms()
	elif sys.argv[1] == "MSS_test":
		MSS_test()
	else:
		print_help()