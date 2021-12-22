#solved with hint from -- https://leetcode.com/problems/largest-component-size-by-common-factor/discuss/819919/Python-Union-find-solution-explained
from collections import deque
import math
class Solution:
    def largestComponentSize(self, nums: List[int]) -> int:
        parents={}
        size={}
        
        #taken
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
            