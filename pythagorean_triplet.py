def triplet(total):
	start=2
	for x in range(1,start):
		y=x+1
		z=y+1
		summation = x+y+z
		while summation<=total:
			while z * z < x * x + y * y:
				z +=1

			if z * z == x * x + y * y:
				mult = x*y*z

		return mult

triplet(12)
