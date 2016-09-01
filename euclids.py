def euclid(m, n):
	while n != 0:
		r = m % n
		m, n = n, r
	return m
			
print(euclid(1))
		