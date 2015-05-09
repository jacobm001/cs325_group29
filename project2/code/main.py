import os
import sys
from project2_rbt import *

def convert_to_array(V):
	V = V.replace("[", "")
	V = V.replace("]", "")
	V = V.replace(" ", "")
	V = V.replace("\n", "")
	V = V.split(',')

	return [int(v) for v in V]


def process_file(fname):
	f = open(fname, 'r')

	save_name = fname.replace(".txt", "")
	w = open(save_name+'change.txt', 'w')

	while True:
		V = f.readline()
		A = f.readline()
		
		if not A: # EOF
			break

		A = int(A)
		V = convert_to_array(V)

		res = changedp(V,A)
		w.write('{0}\n{1}\n'.format(res[0], res[1]))

if __name__ == "__main__":
	if len(sys.argv) != 2:
		print "Argument error"

	if os.path.isfile(sys.argv[1]):
		process_file(sys.argv[1])