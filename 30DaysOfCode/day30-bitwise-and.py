import sys


def find_max(n, k):
	a = b = k

	champ = 0
	for a in range(1, n):
		for b in range(a+1, n+1):
			res = a & b
			if res > champ and res < k:
				champ = res

				if champ == k-1:
					return champ
	return champ

t = int(input().strip())
for a0 in range(t):
    n,k = input().strip().split(' ')
    n,k = [int(n),int(k)]
    print(find_max(n, k))



