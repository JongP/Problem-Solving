#https://justicehui.github.io/ps/2019/04/04/BOJ10986/
#O(n)
#hint  pSum[s] % M = pSum[e] % M



n,m = map(int,input().split())
arr=list(map(int,input().split()))

res=0
#processing prefix
prefix=[0]*n
prefix[0]=arr[0]%m
for i in range(1,n):
    prefix[i]=(prefix[i-1]+arr[i])%m

#cal
dic={i:0 for i in range(m)}

for v in prefix:
    res+=dic[v]
    if v==0:
        res+=1
    dic[v]+=1

print(res)