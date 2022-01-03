#hint from blog
import sys
input=lambda: sys.stdin.readline().rstrip()

#map(int,input().split())
#sys.setrecursionlimit(10**5)

n,l=map(int,input().split())

p=[-1]*l #-1 empty -2 can't insert, i last element to shift
s=[0]*l

def find(num):
    if p[num]<0:
        return num

    p[num]=find(p[num])
    return p[num]

def union(a,b):
    a=find(a)
    b=find(b)

    if s[a]==-1*p[a] and s[b]==-1*p[b]:
        return False 

    if a==b:
        s[a]+=1
        return True

    s[a]+=s[b]+1
    p[a]+=p[b]
    p[b]=a

    return True


for _ in range(n):
    a,b=map(lambda x:int(x)-1,input().split())

    if union(a,b):
        print("LADICA")
    else:
        print("SMECE")
