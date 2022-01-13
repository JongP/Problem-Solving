#solved with hint
#https://www.acmicpc.net/board/view/10157
import sys
from collections import defaultdict
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())

n=int(input())

graph=defaultdict(set)
inDegrees={}
words=[]
for _ in range(n):
    word=input()
    words.append(word)
    for c  in word:
        if c not in inDegrees:
            inDegrees[c]=0


for i in range(n-1):
    for j in range(i+1,n):
        prevWord=words[i]
        word=words[j]
        flag=True
        for k in range(min(len(word),len(prevWord))):
            if word[k]!=prevWord[k]:
                if word[k] not in graph[prevWord[k]]:
                    graph[prevWord[k]].add(word[k])
                    inDegrees[word[k]]+=1
                flag=False
                break
        if flag and len(prevWord)>len(word):
            print("!")
            exit()

    

que=[]
res=[]
for k,v in inDegrees.items():
    if v==0:
        que.append(k)

while que:
    if len(que)>1:
        print("?")
        exit()
    
    cur=que.pop()
    res.append(cur)

    for nextt in graph[cur]: 
        inDegrees[nextt]-=1
        if inDegrees[nextt]==0:
            que.append(nextt)

if len(res)==len(inDegrees.keys()):
    print("".join(res))
else:
    print("!")

#https://www.acmicpc.net/source/19717438
import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)

n=int(input())
words = [[*map(ord,' '.join(input()).split())] for i in range(n)]

adj = [[] for i in range(128)]
visited = [0]*128
cnt = [0]*128

for word in words:
    for ch in word:
        visited[ch] = 1

flag = 0

for i in range(1,n):
    j = 0
    while j < len(words[i-1]) and j < len(words[i]) and words[i-1][j] == words[i][j]: j+=1
    if j < len(words[i-1]) and j >= len(words[i]): flag |= 2
    if j < len(words[i-1]) and j < len(words[i]):
        adj[words[i-1][j]] += [words[i][j]]
        cnt[words[i][j]] += 1

q = [i for i in range(97,123) if cnt[i] == 0 and visited[i]]

res = ''    
while q:
    if len(q) > 1:flag |= 1
    ch = q.pop()
    res += chr(ch)

    for next in adj[ch]:
        cnt[next] -= 1
        if cnt[next] == 0: q.append(next)
if sum(cnt) > 0: flag |= 2
if flag & 2: print('!')    
elif flag & 1: print('?')
else:print(res)