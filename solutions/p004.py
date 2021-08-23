largest = 0
for x in range(1, 1000):
	for y in range(1, 1000):
		prod = x * y
		str1 = str(prod)
		if str1 == str1[::-1]:
			if largest < int(str1):
				largest = int(str1)
print(largest)