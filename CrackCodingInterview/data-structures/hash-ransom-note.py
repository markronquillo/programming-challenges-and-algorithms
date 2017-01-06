def ransom_note(magazine, ransom):
    dct = {}
    for w in magazine:
        dct.setdefault(w, 0)
        dct[w] += 1

    for w in ransom:
        if w not in dct:
            return False

        if dct[w] > 0:
            dct[w] -= 1
        else:
            return False

    return True



m, n = map(int, input().strip().split(' '))
magazine = input().strip().split(' ')
ransom = input().strip().split(' ')
answer = ransom_note(magazine, ransom)

if(answer):
    print("Yes")
else:
    print("No")
    
