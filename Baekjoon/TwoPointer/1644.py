import sys
input = sys.stdin.readline

N= int(input())

if N==1:
    print(0)
    exit()

nums=[]
erathos=[True]*(N+1)
for i in range(2,N+1):
    if erathos[i]:
        nums.append(i)

    j=2
    while i*j<N+1:
        erathos[i*j]=False
        j+=1


#print(nums)
l=len(nums)
answer=0
s=0 
e=0
curSum=nums[0]

while True:
    if curSum<N:
        e+=1
        if e>=l:
            break
        curSum+=nums[e]
    elif curSum>N:
        curSum-=nums[s]
        s+=1
    else:
        answer+=1
        e+=1
        if e>=l:
            break
        curSum+=nums[e]
print(answer)