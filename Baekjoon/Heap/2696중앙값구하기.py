import sys
input=sys.stdin.readline
import heapq
#map(int,input().rstrip().split())
#sys.setrecursionlimit(10**6)

ansL=[]


for _ in range(int(input())):
    m=int(input())
    arr=[-1*int(2e9)]
    lHeap=[]
    rHeap=[]
    answer=[]

    while m>0:
        arr.extend(list(map(int,input().rstrip().split())))
        m-=10

    heapq.heappush(lHeap,arr[1])
    heapq.heappush(rHeap,-1*arr[0])
    answer.append(arr[1])

    for i in range(2,len(arr),2):
        if lHeap[0]>arr[i]:
            heapq.heappush(rHeap,-1*arr[i])
        else:
            heapq.heappush(lHeap,arr[i])

        if lHeap[0]>arr[i+1]:
            heapq.heappush(rHeap,-1*arr[i+1]) 
        else:
            heapq.heappush(lHeap,arr[i+1])           

        if len(lHeap)>len(rHeap):
            l1,l2=lHeap,rHeap
        else:
            l1,l2=rHeap,lHeap

        while(len(l1)>len(l2)):
            heapq.heappush(l2,-1*heapq.heappop(l1))

        answer.append(lHeap[0])

    ansL.append(answer)
    
for ans in ansL:
    print(len(ans))
    for i in range(0,len(ans),10):
        if i+10<len(ans):
            print(" ".join(map(str,ans[i:i+10])))
        else:
            print(" ".join(map(str,ans[i:])))
    
#optimal solution
#https://www.acmicpc.net/source/18948924
from sys import stdin
from heapq import heappush, heappop
read = lambda: stdin.readline().rstrip()

tt = int(read())

for t in range(tt):
    m = int(read())
    arr = [0]

    for i in range(m // 10 + 1):
        arr += list(map(int, read().split()))

    l = []
    r = []
    mid = 0
    res = []

    print(len(arr)//2)

    for i in range(1, len(arr)):
        if i % 2:
            if not r:
                mid = arr[i]
            elif arr[i] <= r[0]:
                heappush(l, arr[i] * (-1))
                mid = heappop(l) * (-1)
            else:
                heappush(r, arr[i])
                mid = heappop(r)
            res.append(mid)

        else: 
            if arr[i] <= mid:
                heappush(l, arr[i] * (-1))
                heappush(r, mid)
            else:
                heappush(r, arr[i])
                heappush(l, mid * (-1))

        if len(res) == 10:
            print(' '.join(map(str, res)))
            res = []

    if res:
        print(' '.join(map(str, res)))