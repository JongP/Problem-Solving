class Solution:
    def numPairsDivisibleBy60(self, time: List[int]) -> int:
        memo=[0]*60
        res=0
        for t in time:
            res+=memo[(60-t%60)%60]
            memo[t%60]+=1

        return res