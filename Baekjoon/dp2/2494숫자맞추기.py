from collections import defaultdict
import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
sys.setrecursionlimit(10**5)

n=int(input())
start=list(map(int,list(input())))
end=list(map(int,list(input())))
dp={}
dpOP={}

def listToNums(l,leftNum):
    res=""
    for i in range(len(l)-leftNum,len(l)):
        res+=str(l[i])
    return res

def rotate(nums,leftNum,left):
    s=n-leftNum
    t=(end[s]-nums[s])%10
    if left:
        #print(s,n,nums)
        for i in range(s,n):
            #print(i)
            nums[i]=(nums[i]+t)%10
        return t
    else:
        nums[s]=(nums[s]-(10-t))%10
        return 10-t

def derotate(nums,leftNum,left,t):
    s=n-leftNum

    if left:
        for i in range(s,n):
            nums[i]=(nums[i]-t)%10
    else:
        nums[s]=(nums[s]+t)%10


def helper(nums,leftNum):
    key=listToNums(nums,leftNum)
    if key in dp:
        return dp[key]

    if leftNum == 0:
        return 0
    
    #to left
    tmp1=rotate(nums,leftNum,True)
    v1=helper(nums,leftNum-1)
    derotate(nums,leftNum,True,tmp1)

    #to right
    tmp2=rotate(nums,leftNum,False)
    v2=helper(nums,leftNum-1)
    derotate(nums,leftNum,False,tmp2)

    if v1+tmp1<v2+tmp2:
        dp[key]=v1+tmp1
        #p1.append(tmp1)
        dpOP[key]=tmp1
        return dp[key]
    else:
        dp[key]=v2+tmp2
        #p2.append(-1*tmp2)
        dpOP[key]=-1*tmp2
        return dp[key]

val=helper(start,n)

print(val)
path=[]
leftNum=n
key=listToNums(start,leftNum)
while leftNum>0:
    t=dpOP[key]
    path.append(t)

    s=n-leftNum
    if t>0:
        for i in range(s,n):
            start[i]=(start[i]+t)%10
    else:
        start[s]=(start[s]+t)%10
    leftNum-=1
    key=listToNums(start,leftNum)

for i,v in enumerate(path):
    if v==0:
        continue
    print(i+1,v)
