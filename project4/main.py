# main.py

import math, os, sys

class City:
	i = None # identity 
	x = None
	y = None

	def __init__(self, i, x, y):
		self.i = i
		self.x = x
		self.y = y

	def distance(self, city):
		x = (self.x - city.x) ** 2
		y = (self.y - city.y) ** 2
		return int(math.sqrt(x+y))

def read_file(file):
	cities = []

	with open(file, 'r') as f:
		for line in f:
			v = line.split(' ')
			cities.append(City(int(v[0]), int(v[1]), int(v[2])))

	return cities

if __name__ == "__main__":
	# sanity check
	if len(sys.argv) != 2:
		print 'Argument Error, please specify an input file.'

	if os.path.exists(sys.argv[1]) == False:
		print 'Argument Error, file, {0}, not found'.format(sys.argv[1])
		sys.exit(0)

	# open output file
	fname = sys.argv[1] + '.tour'
	f = open(fname, 'w')

	# main process
	cities = read_file(sys.argv[1])

	for i in range(0, len(cities)):
		if i < len(cities)-2:
			d = cities[i].distance(cities[i+1])
			f.write('{0}\n'.format(d))

	f.close()