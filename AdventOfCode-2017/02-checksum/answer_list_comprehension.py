import re
import sys


def diffMinMax(arr):
    min_val = sys.maxsize
    max_val = -1
    for v in arr:
        min_val = min_val if min_val < v else v
        max_val = max_val if max_val > v else v
    return max_val - min_val


def solution(input):
    return sum(diffMinMax(line) for line in input)


with open('input.txt', 'r') as f:
    input = []
    for line in f:
        input.append([int(v) for v in re.split('\s*', line) if v != ''])
    print(solution(input))
