#!/usr/bin/py
# Head ends here

# 5 4 3 2 1

def pairs(a,k):
    # a is the list of numbers and k is the difference value
    
    answer = 0
    srtd = sorted(a)[::-1]
    
    for ci, current_val in enumerate(srtd):
        ce = len(srtd) - 1
        while ci < ce:
            diff = current_val - srtd[ce]
            if diff == k:
                answer += 1
                break
            elif diff < k:
                break
            ce -= 1

        if ce == len(srtd) - 1:
            break

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
