def algorithm4(A):
	m1 = m2 = 0

	for x in A:
		m1 = max(0, m1 + x)
		m2 = max(m2, m1)

	return m2
