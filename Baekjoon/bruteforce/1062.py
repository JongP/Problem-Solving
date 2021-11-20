import sys
input = sys.stdin.readline
from itertools import combinations

givenLetters = ['a','n','t','i','c']

n,k = map(int,input().rstrip().split())

alphas=set()
words=[]
for _ in range(n):
    word = set(input().rstrip())

    for letter in givenLetters:
        word.discard(letter)

    if len(word)<=k-5:
        words.append(word)
        alphas=alphas.union(word)

if k<5:
    print(0)
    sys.exit()

max=0
#print(alphas)

iternum=min(len(alphas),k-5)

for letters in combinations(alphas,iternum):
    num=0
    for word in words:
        #print(word)
        flag=True
        for elem in word:
            if elem not in letters:
                flag=False
                break
        if flag:num+=1

    if max<num:
        max=num


print(max)
        
        


