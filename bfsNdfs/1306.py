from collections import deque
class Solution:
    def canReach(self, arr: List[int], start: int) -> bool:
        l=len(arr)
        visited=[0]*l
        que=deque([])
        
        que.append(start)
        
        while que:
            cur=que.popleft()
            if visited[cur]==1:
                continue
            visited[cur]=1
            if arr[cur]==0:
                return True
            
            n1,n2=cur+arr[cur],cur-arr[cur]
            if n1>=0 and n1<l:
                que.append(n1)
            if n2>=0 and n2<l:
                que.append(n2)
        
        return False

    def canReach(self, arr: List[int], start: int) -> bool:
        n = len(arr)
        visited = set()
        queue = [start]
        
        while queue:
            pos = queue.pop(0)
            visited.add(pos)
            
            if arr[pos] == 0:
                return True
            
            p = pos+arr[pos]
            if 0 <= p < n and p not in visited:
                queue.append(p)
            p = pos-arr[pos]
            if 0 <= p < n and p not in visited:
                queue.append(p)
                
        return False