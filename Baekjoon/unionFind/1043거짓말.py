import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
#sys.setrecursionlimit(10**5)

n,m=map(int,input().split())

parents=[i for i in range(n)]

cands=list(map(lambda x:int(x)-1,input().split()))
cand=-1
if cands[0]!=-1:
    cands=cands[1:]
    cand=cands[0]
    for c in cands:
        parents[c]=cand


def find(x):
    if parents[x]==x:
        return x
    parents[x]=find(parents[x])
    return parents[x]

def union(x,y):
    x=find(x)
    y=find(y)
    if x==y:
        return

    if y==cand:
        x,y=y,x
    parents[y]=x


#make union
parties=[]
for _ in range(m):
    party=list(map(lambda x:int(x)-1,input().split()))

    for i in range(1,len(party)-1):
        union(party[i],party[i+1])

    parties.append(party)


#check
res=0

for party in parties:
    if find(party[1])!=cand:
        res+=1

print(res)



#https://www.acmicpc.net/source/12927180
import sys
input = sys.stdin.readline

n, m = map(int, input().split())

k = map(int, input().split())
num = next(k)
fact = list(k)
counted = set(fact)
linked = []
for _ in range(m):
    k = map(int, input().split())
    num = next(k) #to next iterator
    linked.append(set(k))
while fact and linked:
    i = fact.pop()
    new_linked = []
    for k in linked:
        if i in k:
            fact += list(k.difference(counted))
        else:
            new_linked.append(k)
    linked = new_linked

print(len(linked))

#https://www.acmicpc.net/source/17693455
import sys
cnt_party = int(sys.stdin.readline().rstrip().split()[1])
witness_set = set(sys.stdin.readline().rstrip().split()[1:])
party_list = []
possible_list = []
for _ in range(cnt_party):
    party_list.append(set(sys.stdin.readline().rstrip().split()[1:]))
    possible_list.append(1)
for _ in range(cnt_party):
    for i, party in enumerate(party_list):
        if witness_set.intersection(party):
            possible_list[i] = 0
            witness_set = witness_set.union(party)# set.union , set.intersection

print(sum(possible_list))