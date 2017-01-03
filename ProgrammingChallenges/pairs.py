#!/usr/bin/py
# Head ends here
def pairs(a,k):
    answer = 0
    s = set(a)
    for v in s:
        if v+k in s:
            answer +=1

    return answer

# Tail starts here
if __name__ == '__main__':
    a = input().strip()
    a = list(map(int, a.split(' ')))
    _a_size=a[0]
    _k=a[1]
    b = input().strip()
    b = list(map(int, b.split(' ')))
    print(pairs(b,_k))
