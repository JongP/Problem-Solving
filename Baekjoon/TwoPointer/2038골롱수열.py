
#**************how to interpret********************#
n=int(input())

num=3
arr=[0,0,1]

if 1<=n<=3:
    
    print(n//2+1)
    exit()

cur=2
idx=3
prev=3


while True:
    if arr[cur]==0:
        cur+=1
    arr[cur]-=1
    arr.append(cur)
    idx+=cur

    if prev<n<=idx:
        print(len(arr)-1)
        exit()

    prev=idx
    num+=1