from collections import deque

def solution(n, computers):
    answer = 0
    cnt=0
    visited=[0]*n
    queue=deque()

    while(cnt!=n):
        for i in range(n):
            if(visited[i]==0):
                visited[i]=1
                queue.append(i)
                cnt+=1
                answer+=1
                break

        while queue:
            cur=queue.popleft()
            for i in range(n):
                if computers[cur][i] ==1 and visited[i]==0:
                    visited[i]=1
                    cnt+=1
                    queue.append(i)


    



    return answer
print(solution(3,[[1, 1, 0], [1, 1, 1], [0, 1, 1]]))