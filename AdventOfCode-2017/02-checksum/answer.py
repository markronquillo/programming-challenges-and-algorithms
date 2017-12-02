import re
import sys


def solution(input):
    checksum = 0
    for line in input:
        min = sys.maxsize
        max = -1
        for v in line:
            try:
                v = int(v)
                min = min if min < v else v
                max = max if max > v else v
            except:
                pass
        checksum += (max - min)
    return checksum


with open('input.txt', 'r') as f:
    input = []
    for line in f:
        input.append(re.split('\s*', line))
    print(solution(input))
