#도둑질
#https://programmers.co.kr/learn/courses/30/lessons/42897
def solution(money):
    answer = 0
    l=len(money)
    dp=[[0]*l for _ in range(2)]


        
    dp[0][0]=money[0]
    dp[0][1]=0
    dp[1][1]=money[1]
        

    dp[0][2]=max(dp[0][1],dp[0][0]+money[2])
    dp[1][2]=max(dp[1][1],dp[1][0]+money[2])

    for i in range(3,l):
        dp[0][i]=max(max(dp[0][i-1],dp[0][i-2]+money[i]),dp[0][i-3]+money[i])
        dp[1][i]=max(max(dp[1][i-1],dp[1][i-2]+money[i]),dp[1][i-3]+money[i])

   
    



    return max(dp[0][-2],dp[1][-1])


print(solution([10, 2, 2, 100, 1]))