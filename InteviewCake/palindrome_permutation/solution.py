

val = "raccar"

dct = {}

for c in val:
    if c in dct.keys():
        dct[c] += 1
    else:
        dct[c] = 1

odds_allowed = 1
for k, v in dct.items():
    if v % 2 == 1:
        odds_allowed -= 1

    if odds_allowed < 0:
        break

if odds_allowed < 0:
    print("False")
else:
    print("True")


