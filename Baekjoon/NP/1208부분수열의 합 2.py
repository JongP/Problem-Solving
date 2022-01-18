#new concept
#meet in the middle
#O(2^(N/2 +Nlog(N)+N)
N,S=map(int,input().split())
arr=list(map(int,input().split()))
pivot=len(arr)//2

def getCombSum(arr,s,e,path,res):
    if s>e:
        res.append(path)
        return

    getCombSum(arr,s+1,e,path,res)
    getCombSum(arr,s+1,e,path+arr[s],res)
    
#meet in the middle
leftSum=[]
rightSum=[]
getCombSum(arr,0,pivot-1,0,leftSum)
getCombSum(arr,pivot,len(arr)-1,0,rightSum)

leftSum.sort()
rightSum.sort(reverse=True)

#print(leftSum,rightSum)
idx1=idx2=0
res=0 if S!=0 else -1
while idx1<len(leftSum) and idx2<len(rightSum):
    total=leftSum[idx1]+rightSum[idx2]
    if total>S:
        idx2+=1
    elif total<S:
        idx1+=1
    else:#most important part
        tmp1=idx1;tmp2=idx2
        while idx1<len(leftSum) and leftSum[idx1]==leftSum[tmp1]: idx1+=1
        while idx2<len(rightSum) and rightSum[idx2]==rightSum[tmp2]: idx2+=1
        res+=(idx1-tmp1)*(idx2-tmp2)

#print(leftSum,rightSum)
print(res)