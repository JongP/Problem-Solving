#https://leetcode.com/discuss/general-discussion/1125779/Dynamic-programming-on-subsets-with-examples-explained

class Solution:
    def makesquare(self, matchsticks: List[int]) -> bool:
        """
        length of one side = sum(matchsticks)//4 if sum(matchsticks)%4 --> retunr Fasle
        -->targetSum
        can group the matchsticks with 4 groups summed to targetSum
        
        recursion -- curSum, leftGroup, visited
        1 1 2 4 6 8 2
        0,4,0
        """
        total=sum(matchsticks)
        if total%4!=0: return False
        targetSum=total//4
        l=len(matchsticks)
        
        
        matchsticks.sort(reverse=True)
        
        
        
        memo=set()
        def canMake(idx,groups):
            key=tuple(sorted(groups))
            
            if idx==l:
                return True
            elif (idx,key) in memo:
                return False
            
            for i in range(4):
                if groups[i]+matchsticks[idx]<=targetSum:
                    groups[i]+=matchsticks[idx]
                    if canMake(idx+1,groups):
                        return True
                    groups[i]-=matchsticks[idx]
            
            memo.add((idx,key))
                    
            return False
        
        
        
        
        groups=[matchsticks[0],0,0,0]
        return canMake(1,groups) if matchsticks[0]<=targetSum else False
        
        
        
#https://leetcode.com/discuss/general-discussion/1125779/Dynamic-programming-on-subsets-with-examples-explained
class Solution:
    def makesquare(self, nums):
        N = len(nums)
        basket, rem = divmod(sum(nums), 4)
        if rem or nums[0] > basket: return False
        
        @lru_cache(None)
        def dfs(mask):
            if mask == 0: return 0
            for j in range(N):
                if mask & 1<<j:
                    neib = dfs(mask ^ 1<<j)
                    if neib >= 0 and neib + nums[j] <= basket:
                        return (neib + nums[j]) % basket
            return -1
                    
        return dfs((1<<N) - 1) == 0