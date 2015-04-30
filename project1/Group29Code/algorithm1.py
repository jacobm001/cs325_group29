def algorithm1(A):
	max = 0
	for i in range(0, len(A)):
		for j in range(i, len(A)):
			partial = 0
			for k in range(i, j+1):
				partial += A[k]

			if partial > max:
				max = partial

	return max
