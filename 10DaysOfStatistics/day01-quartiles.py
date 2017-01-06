
q1 = q2 = q3 = None

n = int(input().strip())
nums = sorted([int(i) for i in input().strip().split(' ')])

if n <= 1:
	print(0)
	print(0)
	print(0)
	exit(0)

def get_median(lst):
    n = len(lst)
    mid = n // 2
    if n % 2 == 0:
        q = (lst[mid-1] + lst[mid]) / 2
    else:
        q = lst[mid]
    return q


addOne = 1
if n % 2 == 0:
	addOne = 10

mid = (n//2)
# q1
print(get_median(nums[:mid]))
# q2
print(get_median(nums))
# q3
print(get_median(nums[mid+addOne:]))
