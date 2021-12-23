#solved with hint from -- https://leetcode.com/problems/largest-component-size-by-common-factor/discuss/819919/Python-Union-find-solution-explained
from collections import deque
import math
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        parents={}
        size={}
        
        #taken
        #you have to know this separately
        def primes_set(n):
            for i in range(2, int(math.sqrt(n))+1):
                if n % i == 0:
                    return primes_set(n//i) | set([i])
            return set([n])
        
        def find(parents,size,node):
            if node not in parents:
                parents[node]=node
                size[node]=0
            
            if parents[node]==node:
                return node    
            parents[node]=find(parents,size,parents[node])
            return parents[node]
        
        def union(parents,size,a,b):
            a=find(parents,size,a)
            b=find(parents,size,b)
            
            if a==b:
                return
            
            parents[b]=a
            size[a]+=size[b]
        

        for num in nums:
            mySet=primes_set(num)
            for prime in mySet:
                for tmp in mySet:
                    union(parents,size,prime,tmp)
            r=find(parents,size,mySet.pop())   
            size[r]+=1
            
                
        return max(size.values())



#optimal solution from the link
class DSU:
    def __init__(self, N):
        self.p = list(range(N))

    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]

    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        self.p[xr] = yr

# Our disjoint set
class DSU:
    def __init__(self, N):
        self.p = list(range(N))
	# keep finding til we reach the parent
    def find(self, x):
        if self.p[x] != x:
            self.p[x] = self.find(self.p[x])
        return self.p[x]
        
	# point y to x (x as parent)
    def union(self, x, y):
        xr, yr = self.find(x), self.find(y)
        self.p[xr] = yr

class Solution:
	# Function to generate primes set for number n
    def primes_set(self,n):
        for i in range(2, int(math.sqrt(n))+1):
            if n % i == 0:
                return self.primes_set(n//i) | set([i])
        return set([n])
        
    def largestComponentSize(self, A):
        n = len(A)
        UF = DSU(n)
        primes = defaultdict(list)
        # calculate primes set for all elements in A
        for i, num in enumerate(A):
            pr_set = self.primes_set(num)
            for q in pr_set: primes[q].append(i)
		# union disjoint set based on same primes
        for _, indexes in primes.items():
            for i in range(len(indexes)-1):
                UF.union(indexes[i], indexes[i+1])
		# Count the apperance of parents, return the maxium one
		# Since all connected nodes will point to same parent
        return max(Counter([UF.find(i) for i in range(n)]).values())