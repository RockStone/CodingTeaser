def max_sum(a):
	x, y, z = [0] * 3
	for i in a:
		print i, x, y, z
		x += i
		if y > x:
			y = x
		if z < (x - y):
			z = (x - y)
	return z

if __name__ == "__main__":
	a = [2, 3, 1, -7, 0, -5, 4, -1, -1, 6]

	print max_sum(a)
