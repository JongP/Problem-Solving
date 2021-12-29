n=input()
arr=list(map(int,input().split()))
tmpL=sorted(list(set(arr)))
dic={tmpL[i]:i  for i in range(len(tmpL))}

for i in range(len(arr)):
    arr[i]=dic[arr[i]]

print(" ".join(map(str,arr)))


