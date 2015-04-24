def algorithm1(A):
	max = 0
	for i in range(0, len(A)):
		for j in range(i, len(A)):
			partial = 0
			for j in range(i, j):
				partial += A[j]

			if partial > max:
				max = partial

	return max