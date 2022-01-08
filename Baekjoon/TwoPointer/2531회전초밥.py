import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
#sys.setrecursionlimit(10**5)
n,d,k,c=map(int,input().split())

arr=[int(input()) for _ in range(n)]
arr.extend(arr[:k-1])



dic={}
for i in range(k):
    dic[arr[i]]=dic.get(arr[i],0)+1


res=len(dic.keys())#check
cur=res
if dic.get(c,0)==0:
    res+=1

le=1
ri=k
while ri <len(arr):

    dic[arr[le-1]]-=1
    if dic[arr[le-1]]==0:
        cur-=1

    dic[arr[ri]]=dic.get(arr[ri],0)+1
    if dic[arr[ri]]==1:
        cur+=1
    
    cwc=cur+1 if dic.get(c,0)==0 else cur
    if cwc>res:
        res=cwc
    le+=1
    ri+=1


print(res)

#- Solution link: http://www.teferi.net/ps/problems/boj/2531
#u can use array with size d not dictionary
import itertools
import sys


def main():
    N, d, k, c = [int(x) for x in sys.stdin.readline().split()]
    nums = [int(sys.stdin.readline()) for _ in range(N)]

    counter = [0] * (d + 1)
    counter[c] = 1
    for num in nums[:k]:
        counter[num] += 1
    answer = size = sum(1 for x in counter if x > 0)
    for l, r in zip(nums, itertools.chain(nums[k:], nums)):
        counter[l] -= 1
        if counter[l] == 0:
            size -= 1
        counter[r] += 1
        if counter[r] == 1:
            size += 1
        answer = max(answer, size)

    print(answer)