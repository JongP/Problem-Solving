import sys
ip = sys.stdin.readline

def w(a,b,c):
    global dp

    #print(idx_a,idx_b,idx_c)
    if a<=0 or b<=0 or c<=0 :
        return 1
    if a>20 or b>20 or c>20 :
        return w(20,20,20)

    if dp[a][b][c] != -1:
        return dp[a][b][c]

    if a<b and b<c:
        dp[a][b][c] =w(a,b,c-1)+w(a,b-1,c-1)-w(a,b-1,c)
        return dp[a][b][c]

    dp[a][b][c]=w(a-1,b,c)+w(a-1,b-1,c)+w(a-1,b,c-1)-w(a-1,b-1,c-1)
    return dp[a][b][c]

ansList=[]
dp= [[[-1 for _ in range(51)] for _ in range(51)] for _ in range(51)]
dp[0][0][0]=1

while True:
    a,b,c = tuple(map(int,ip().rstrip().split()))
    if a==-1 and b==-1 and c==-1 :
        break
    ans= w(a,b,c)
    ansList.append((str(a),str(b),str(c),str(ans)))
    

for a,b,c,ans in ansList:
    print("w("+a+", "+b+", "+c+") = "+ans)