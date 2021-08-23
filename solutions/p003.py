num = 600851475143

largest = 2
while num > largest:
	if num % largest == 0:
		num /= largest
	else:
		largest += 1

print(largest)
