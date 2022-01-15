
class Solution:
    def minJumps(self, arr: List[int]) -> int:
        
        #O(n), O(n)
        l=len(arr)

        
        dic={}
        
        
        for i in range(l):
            if arr[i] not in dic:
                dic[arr[i]]=[]
                
            dic[arr[i]].append(i)
        
            
        
        
        dp=[-1]*l
        visited=set()
        valVisited=set()
        que=[0]
        cnt=0
        
        
        while True:
            tmp=[]
            while que:
                cur=que.pop()
                if cur==l-1:
                    return cnt
                
                if cur+1<l and cur+1 not in visited:
                    visited.add(cur+1)
                    tmp.append(cur+1)
                    
                if cur-1>=0 and cur-1 not in visited:
                    visited.add(cur-1)
                    tmp.append(cur-1)
                
                if arr[cur] in valVisited:
                    continue
                valVisited.add(arr[cur]) 
                
                for nxt in dic[arr[cur]]:#I fisrt misestimated time complexity!!
                    if dp[nxt] not in visited:
                        visited.add(nxt)
                        tmp.append(nxt)
            cnt+=1
            que=tmp


#exmaple solution
    def minJumps(self, arr: List[int]) -> int:
        val_to_idx = collections.defaultdict(list)
        n = len(arr)
        
        for i in range(n):
            val_to_idx[arr[i]].append(i)
        
        queue = collections.deque([0])
        visited = set()
        visited.add(0)
        steps = 0
        
        while queue:
            size = len(queue)
            for _ in range(size):
                idx = queue.popleft()
                val = arr[idx]
                if idx == n-1:
                    return steps
                
                for nxt in [idx+1, idx-1] + val_to_idx[val]:
                    if nxt < 0 or nxt >= n or nxt in visited:
                        continue
                    visited.add(nxt)
                    queue.append(nxt)
                del val_to_idx[arr[idx]] # to avoid TLE #you can delete it
            steps += 1
        