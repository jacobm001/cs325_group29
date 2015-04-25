def algorithm3(A):
	if len(A) < 1:
		return 0

	m = len(A) / 2

	lmax = s = 0
	for i in range(len(A)/2, -1, -1):
		s += A[i]
		if s > lmax:
			lmax = s

	rmax = s = 0
	for i in range(len(A)/2+1, len(A)):
		s += A[i]
		if s > rmax:
			rmax = s

	return max(
		algorithm3(A[:len(A)/2]),
		algorithm3(A[(len(A)/2)+1:]),
		lmax + rmax
	)
