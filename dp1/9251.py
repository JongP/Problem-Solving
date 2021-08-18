import sys
input = sys.stdin.readline

n= input().rstrip()
key= input().rstrip()
l=len(n)
l2= len(key)

dp=[[0,0] for _ in range(l)] #[length,index in key]

for i in range(l):

    idxList=[]
    #for the past
    for j in range(i):
        #longer
        if dp[i][0]>dp[j][0]+1:
            idx=-1
             #hasPlace
            for k in range(dp[j][1],l2):
                if n[i]==key[k]:
                    idx=k
                    break
            if idx==-1: continue
            dp[i][0]=dp[j][0]+1
            dp[i][1]=idx
       
