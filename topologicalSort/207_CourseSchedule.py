from collections import deque,defaultdict
#is it cyclic or acyclic
class Solution:
    #Khan's topological sort O(V+E)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        que=deque()
        graph=defaultdict(list)
        cnt=0
        inDegrees=[0]*numCourses
        
        for a,b in prerequisites:
            inDegrees[a]+=1
            graph[b].append(a)
            
            
        for i,v in enumerate(inDegrees):
            if v==0:
                que.append(i)
                cnt+=1

        
        while que:
            cur=que.popleft()
            
            for nxt in graph[cur]:
                if inDegrees[nxt]==0:
                    continue
                inDegrees[nxt]-=1
                if inDegrees[nxt]==0:
                    que.append(nxt)
                    cnt+=1
                
                
        if cnt!=numCourses:
            return False
        return True
    #DFS topological sort O(V+E)
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        self.graph = [[] for _ in range(numCourses)]
        self.visited = [0] * numCourses

        for pre in prerequisites:
            self.graph[pre[0]].append(pre[1])

        def dfs(courseNum):
            if self.visited[courseNum] == -1: return False#meaning courseNum's ancestor
            if self.visited[courseNum] == 1: return True#meaning common descendant

            self.visited[courseNum] = -1

            for course in self.graph[courseNum]:
                if not dfs(course): return False
            
            self.visited[courseNum] = 1
            return True
        
        for courseNum in range(numCourses):
            if not dfs(courseNum): return False
        
        return True
            
#https://www.geeksforgeeks.org/topological-sorting-indegree-based-solution/?ref=lbp
#https://leetcode.com/problems/course-schedule/discuss/162743/JavaC%2B%2BPython-BFS-Topological-Sorting-O(N-%2B-E)
#https://leetcode.com/problems/course-schedule/discuss/203028/Python-solution