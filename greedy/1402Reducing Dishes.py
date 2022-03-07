class Solution:
    def maxSatisfaction(self, satisfaction: List[int]) -> int:
        satisfaction.sort(reverse=True)

        res=0
        prefixSum=0

        for num in satisfaction:
            prefixSum+=num
            
            if res>res+prefixSum:
                return res
            
            res+=prefixSum

        return res