sum=2
for x in range(2, 1000):
	if (x == 2):
		term = 3
		min1 = 2
		min2 = 1
	else :
		min2 = min1
		min1 = term
		term = min1 + min2

	if (term % 2 == 0):
		sum += term

	if (term >= 4000000):
		break
print(sum)