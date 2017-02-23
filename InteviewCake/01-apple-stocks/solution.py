
lst = [10, 7, 5, 8, 11, 9]
s = -1
champ = -1
for i in range(1, len(lst)):
    if s == -1 and lst[i-1] < lst[i]:
        s = i-1

    if s > -1 and (lst[i-1] > lst[i] or len(lst) == i+1):
        if lst[i-1] > lst[i]:
            e = i - 1
        else:
            e = i
        val = lst[e] - lst[s]
        print(lst[e], lst[s])
        if val > champ:
            champ = val

print(champ)
