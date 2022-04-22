class Solution:
    def mctFromLeafValues(self, arr: List[int]) -> int:
        memo={}
        
        def dp(i,j):
            if i==j:
                return 0,arr[i]
            elif (i,j) in memo:
                return memo[(i,j)]
            
            total=math.inf
            maxV=0
            
            for k in range(i,j):
                lSum,lMax=dp(i,k)
                rSum,rMax=dp(k+1,j)
                if lSum+rSum+lMax*rMax<total:
                    total =lSum+rSum+lMax*rMax
            
                maxV=max(lMax,rMax)
            
            memo[(i,j)]=(total,maxV)
            return total,maxV
        
        return dp(0,len(arr)-1)[0]


#https://leetcode.com/problems/minimum-cost-tree-from-leaf-values/discuss/339959/One-Pass-O(N)-Time-and-Space
    def mctFromLeafValues(self, A):
        res = 0
        stack = [float('inf')]
        for a in A:
            while stack[-1] <= a:
                mid = stack.pop()
                res += mid * min(stack[-1], a)
            stack.append(a)
        while len(stack) > 2:
            res += stack.pop() * stack[-1]
        return res