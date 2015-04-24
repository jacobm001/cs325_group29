def algorithm2(A):
	max = 0
	for i in range(0, len(A)):
		sum = 0
		for j in range(i, len(A)):
			sum = sum + A[j]
			if max <= sum:
				max = sum

	return max
