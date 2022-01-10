#unsolved
#hint from blog
#https://blog.naver.com/PostView.naver?blogId=kks227&logNo=220795165570&categoryNo=299&parentCategoryNo=0&viewDate=&currentPage=9&postListTopCurrentPage=1&from=postList&userTopListOpen=true&userTopListCount=5&userTopListManageOpen=false&userTopListCurrentPage=9

import sys
input=lambda: sys.stdin.readline().rstrip()
#map(int,input().split())
#sys.setrecursionlimit(10**5)

n,k=map(int,input().split())
coins=[int(input()) for _ in range(n)]

cur=[0 for _ in range(k+1)]
cur[0]=1

for i in range(n):
    val=coins[i]
    for j in range(k+1):
        if j-val>=0:
            cur[j]+=cur[j-val]
    #print(val,cur)

#[print(line) for line in dp]
print(cur[-1])