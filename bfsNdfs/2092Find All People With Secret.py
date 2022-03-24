#sovled with one hint
#Could you model all the meetings happening at the same time as a graph?
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        known=set([0,firstPerson])
        
        meetings.sort(key=lambda x:x[2])
        meetings.append((0,0,math.inf))
        
            
        cur=-1
        starts=set()
        graph=collections.defaultdict(set)
        
        for x,y,t in meetings:
            if cur<t:
                visited=set()
                for s in starts:
                    if s not in visited:
                        self.dfs(s,graph,visited,known)
                    
                cur=t
                graph.clear()
                starts.clear()
                visited.clear()
                

            graph[x].add(y)
            graph[y].add(x)
            if x in known: starts.add(x)
            if y in known: starts.add(y)
        
        
        return list(known)
    

    def dfs(self,node,graph,visited,known):
        stk=[node]
        
        while stk:
            cur=stk.pop()
            visited.add(cur)
            known.add(cur)
            
            for nxt in graph[cur]:
                if nxt not in visited:
                    stk.append(nxt)
            
#https://leetcode.com/problems/find-all-people-with-secret/discuss/1599870/Python3-BFS-or-DFS-by-group
#BFS GROUPBY
class Solution:
    def findAllPeople(self, n: int, meetings: List[List[int]], firstPerson: int) -> List[int]:
        can = {0, firstPerson}
        for _, grp in groupby(sorted(meetings, key=lambda x: x[2]), key=lambda x: x[2]): 
            queue = set()
            graph = defaultdict(list)
            for x, y, _ in grp: 
                graph[x].append(y)
                graph[y].append(x)
                if x in can: queue.add(x)
                if y in can: queue.add(y)
                    
            queue = deque(queue)
            while queue: 
                x = queue.popleft()
                for y in graph[x]: 
                    if y not in can: 
                        can.add(y)
                        queue.append(y)
        return can
        
        
        