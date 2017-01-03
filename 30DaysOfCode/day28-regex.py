
import sys, re


N = int(input())
lst = []
for a0 in range(N):
    firstName,emailID = input().split(' ')
    firstName,emailID = [str(firstName),str(emailID)]
    if re.match(r'[\w\d\._-]+@gmail\.com$', emailID):
    	lst.append(firstName)

print("\n".join(sorted(lst)))