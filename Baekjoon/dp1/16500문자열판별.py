import sys
input= sys.stdin.readline

s=input().rstrip()
n=int(input())
A=[]
dp=[1]*(len(s)+1)

for _ in range(n):
    A.append(input().rstrip())

def helper(s,idx):
    if dp[idx]==0:
        return False

    if idx==len(s):
        return True

    for word in A:
        for i,v in enumerate(word):
            if idx+i>=len(s) or v!=s[idx+i] :
                break
            if i==len(word)-1:
                if helper(s,idx+i+1):
                    return True
    dp[idx]=0
    return False




print([0,1][helper(s,0)])