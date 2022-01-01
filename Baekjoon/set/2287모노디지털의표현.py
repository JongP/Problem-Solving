import sys
from collections import defaultdict
input=sys.stdin.readline

k=int(input())
ansL=[]
#build nums
nums=defaultdict(set)
nums[1].add(k)

for i in range(1,9):
    for j in range(1,i//2+1):
        for e1 in nums[j].copy():
            for e2 in nums[i-j].copy():
                nums[i].add(e1+e2)
                nums[i].add(abs(e1-e2))
                nums[i].add(e1*e2)
                if e1!=0 and e2!=0:
                    nums[i].add(e1//e2)
                    nums[i].add(e2//e1)
                                 
    nums[i].add(int("1"*i)*k)
visited=None

for _ in range(int(input())):
    n=int(input())
    ansL.append("NO")

    for i in range(1,9):
        if n in nums[i]:
            ansL[-1]=i
            break



[print(a) for a in ansL]