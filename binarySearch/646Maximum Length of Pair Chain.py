class Solution:
    #nlogn
    def findLongestChain(self, pairs: List[List[int]]) -> int:
        pairs.sort(key= lambda x: (x[1],x[0]))
        
        dp=[0]*len(pairs)
        dp[0]=1
        
        for i, (a,b) in enumerate(pairs[1:],start=1):
            s= self.myBisect(pairs,i)
            dp[i]=max(dp[i-1],(dp[s] if s!=-1 else 0 )+1)
        
        return dp[-1]
    
    def myBisect(self,pairs,idx):
        le,ri=0,idx-1
        res=-1
        start=pairs[idx][0]
        
        while le<=ri:
            mid=(le+ri)//2
            
            if pairs[mid][1]<start:
                res=mid
                le=mid+1
            else:
                ri=mid-1
                
        return res

#greeddy withouth binary search
#https://leetcode.com/problems/maximum-length-of-pair-chain/discuss/225801/Proof-of-the-greedy-solution
class Solution:
    def findLongestChain(self, pairs):
        N = len(pairs)
        pairs.sort(key = lambda x: x[1])
        ans = 0
        cur = -math.inf
        for head, tail in pairs:
            if head > cur:
                cur = tail
                ans += 1
        return ans