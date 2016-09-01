import sys
import math

def is_prime(n):
	for i in range(2, int(math.sqrt(n)+1)):
		if n % i == 0:
			return False
	return True


def nth_prime(n):
	count = 0
	for i in range(2,100000):
		if is_prime(i):
			count += 1
		if count == n:
			return i
			


if __name__ == '__main__':
	if len(sys.argv) < 2:
		print("Usage : python prime.py <nth number>")
	else:
		n = sys.argv[1]
		try:
			n = int(n)
			print(nth_prime(n))
		except ValueError:
			print("invalid input. please enter a valid integer")
		
		
		