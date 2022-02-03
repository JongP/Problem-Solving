#meet in the middle like

from collections import defaultdict
class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        n=len(nums1)
        res=0
        
        dic=defaultdict(int)
        
        for n1 in nums1:
            for n2 in nums2:
                dic[n1+n2]+=1
        for n3 in nums3:
            for n4 in nums4:
                res+=dic[-1*(n3+n4)]
        return res