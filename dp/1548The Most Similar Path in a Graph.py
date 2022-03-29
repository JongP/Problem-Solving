class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targetPath: List[str]) -> List[int]:
        graph= self.buildGraph(n,roads)
        
        memo={}

        def dfs(node,path,dist):
            depth=len(path)
            if depth==len(targetPath):
                return 0
            elif (node,depth) in memo:
                return memo[(node,depth) ][1]
            
            
            
            minDist=math.inf
            
            for nxt in graph[node]:
                
                path.append(nxt)
                
                val=dfs(nxt,path,dist)+(1 if names[nxt]!=targetPath[depth] else 0)
                if val<minDist:
                        minNode=nxt
                        minDist=val
                    
                path.pop()
                        
            memo[(node,depth)]=(minNode,minDist)
            
            return minDist
            
        dfs(n,[],0)

        res=[]
        cur=n
        for i in range(len(targetPath)):
            nxtNode,_=memo[(cur,i)]
            res.append(nxtNode)
            cur=nxtNode
        return res
            
        
        
        
        
    def buildGraph(self,n,roads):
        graph=[[] for _ in range(n+1)]
        
        for a, b in roads:
            graph[a].append(b)
            graph[b].append(a)
            
        graph[n][:]=[i for i in range(n)]
            
        return graph
                
#dikstra
#https://leetcode.com/problems/the-most-similar-path-in-a-graph/discuss/1011732/Python-dijakstra-with-heap-and-set
class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], targets: List[str]) -> List[int]:
        graph = defaultdict(list)
        heap = []
        
		# building graph with adjencency list 
        for x, y in roads:      # O(n+e) time, space
            graph[x] += [y]
            graph[y] += [x]
        
		# adding each node as starting to min heap (by default, all operations done on heapq module (our heap) support min heap)
		# (0, 0, i, [i]) means (edit_cost, node_nb_in_targets/level, city_nb, [path_so_far])
        for i in range(n):     # O(n) time
            heapq.heappush(heap, (0, 0, i, [i]))     # O(logn) time, O(n) space
			
        #seen set to prevent recomputing the same entires multiple times
        seen = set()
        while heap:    # O(len(t) * n) time, space - for every node in targets we have n-1 ~ n neighbours at most
            ed, i, city_nb, path = heapq.heappop(heap) O(logn)
			
			# -i because when adding to out min heap, we will be using negative indexing. Why? To extract the most possible path with
			# min edit distanceas soon as possible. Consider 3 following entries in heap:
			#    (1,-3, _, _)
			#    (1, -2, _, _)
			#    (2, -2, _, _)
			# Entry 1 and2 have the best edit distance so far. They are on 3rd (-3) and 2nd (-2) levels (nodes in target). 
			# That means we want to process (1,-3, _, _) first because it went further down the target path with the same
			# edit distance as (1, -2, _, _), so the chance of getting the best result (in our case min edit distance) are
			# higher in first, rather than second case. Since we use min heap, negative indexing is needed for the best result.
			
            if -i == len(targets):
                return path[:-1] #one last element in path is always redundant as it was added one level before
				
			#  if current city we are considering is different that city in targets at corresponding level, edit dist has to be increased
            if names[city_nb] != targets[-i]: 
                ed += 1
            
            for nbr in graph[city_nb]: 
			    # if we did not process a node 'nbr' on 'i'th-1 level with 'ed' edit distance, let's add it as a possibilty for a path 
                if (ed, i-1, nbr) not in seen:
                    heapq.heappush(heap, (ed, i-1, nbr, path + [nbr])) # add current ed, one level deeper (negative indexing, remember!), neighbouring node, and path so far
                    seen.add((ed, i-1, nbr))
        return 0

            

#Bottom up dp
#https://leetcode.com/problems/the-most-similar-path-in-a-graph/discuss/790240/Python-Clean-bottom-up-DP-solution-with-explanation-O(N2-*-len(tp))
class Solution:
    def mostSimilar(self, n: int, roads: List[List[int]], names: List[str], tp: List[str]) -> List[int]:
        # construct graph
        graph = [[] for _ in range(n)]
        for u, v in roads:
            graph[u].append(v)
            graph[v].append(u)
        
        # init variables
        m = len(tp)
        dp = [[m] * n for _ in range(m)]
        prev = [[0] * n for _ in range(m)]
        
        # populate dp
        for v in range(n):
            dp[0][v] = (names[v] != tp[0])
        for i in range(1, m):
            for v in range(n):
                for u in graph[v]:
                    if dp[i-1][u] < dp[i][v]:
                        dp[i][v] = dp[i-1][u]
                        prev[i][v] = u
                dp[i][v] += (names[v] != tp[i])
                
        # re-construct path
        path, min_dist = [0], m
        for v in range(n):
            if dp[-1][v] < min_dist:
                min_dist = dp[-1][v]
                path[0] = v
        for i in range(m - 1, 0, -1):
            u = prev[i][path[-1]]
            path.append(u)
            
        return path[::-1]