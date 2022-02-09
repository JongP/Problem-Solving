from collections import defaultdict
class Solution:
    def findPairs(self, nums: List[int], k: int) -> int:
        found=set()
        pairs=set()
        
        for num in nums:
            if num+k in found: pairs.add((num,num+k))
            if num-k in found: pairs.add((num-k,num))
            
            found.add(num)
        
        return len(pairs)