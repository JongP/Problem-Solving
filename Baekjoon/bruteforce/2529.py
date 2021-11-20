from itertools import permutations
import sys
input = sys.stdin.readline

numbers=[9,8,7,6,5,4,3,2,1,0]

k = int(input())
ineqauls = input().rstrip().split()
#print(ineqauls)
ansList=[]
for permut in permutations(numbers,k+1) :
    flag=True
    for i in range(k):
        if ineqauls[i]=='>' and permut[i]<permut[i+1]:
            flag=False
            break
        if ineqauls[i]=='<' and permut[i]>permut[i+1]:
            flag=False
            break
    if flag:
        ansList.append("".join(list(map(str,permut))))
#print(ansList)
print(ansList[0])
print(ansList[-1])