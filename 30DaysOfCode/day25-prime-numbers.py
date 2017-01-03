import math


def isPrime(num):
    i = 3
    while (i <= math.sqrt(num)):
        if num % i == 0:
            return False
        i += 2
    return True


T=int(input())
for i in range(T):
    data=int(input())
    if isPrime(data):
    	print("Prime")
    else:
    	print("Not prime")
