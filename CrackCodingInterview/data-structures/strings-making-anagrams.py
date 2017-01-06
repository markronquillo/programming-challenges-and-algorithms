def number_needed(a, b):
	less = 97
	lst_count = [0] * 26
	
	# count every 	
	for c in a:
		lst_count[ord(c) - less] += 1

	for c in b:
		ind = ord(c) - less
		lst_count[ind] -= 1

	return sum([abs(n) for n in lst_count])

a = input().strip()
b = input().strip()

print(number_needed(a, b))

