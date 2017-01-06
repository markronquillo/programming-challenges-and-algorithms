def is_matched(expression):
	n = len(expression)

	if n % 2 != 0:
		return False

	stack = []

t = int(input().strip())
for a0 in range(t):
    expression = input().strip()
    if is_matched(expression) == True:
        print("YES")
    else:
        print("NO")
