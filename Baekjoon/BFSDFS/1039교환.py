n,k=map(int,input().split())
m=len(str(n))

arr=[ n//(10**i)-10*(n//(10**(i+1)))   for i in range(m-1,-1,-1)]
#print(arr)
if len(arr)==1:
    print(-1)
    exit()
if len(set(arr))!=len(arr):
    flag=True
else: flag=False

def arrToNum(arr):
    num=0
    arr.reverse()
    for i in range(len(arr)):
        num+=arr[i]*(10**i)
    return num

cnt=m
while cnt>0:
    tmpV=max(arr[-1*cnt:])

    tmpI=arr[-1*cnt:][::-1].index(tmpV)
    #print(arr,tmpV,tmpI)
    if tmpI==cnt-1:
        cnt-=1
        continue
    tmpI=m-tmpI-1

    #print(arr[-1*cnt:],cnt,tmpV)
    arr[-1*cnt],arr[tmpI]=arr[tmpI],arr[-1*cnt]
    #print(arr)
    k-=1
    cnt-=1
    if(k==0):
        print(arrToNum(arr))
        exit(0)

if flag:
    print(arrToNum(arr))
elif arr[1]==0:
    print(-1)
elif  k%2==0:
    print(arrToNum(arr))
else:
    arr[-1],arr[-2]=arr[-2],arr[-1]
    print(arrToNum(arr))
#52676 2