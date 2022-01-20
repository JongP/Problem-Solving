#O(n*logn) O(1)
class Solution:
    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        
        le=1
        ri=max(piles)*len(piles)
        
        
        
        def isPossible(x):
            res=0
            for pile in piles:
                res+=math.ceil(pile/x)
            return res<=h
        
        while le<ri:
            mid=(le+ri)//2
            
            if isPossible(mid):
                ri=mid
            else:
                le=mid+1
        
        
        return ri


    def minEatingSpeed(self, piles: List[int], h: int) -> int:
        def check(current_k):
            count = 0
            for pile in piles:
                count += math.ceil(pile / current_k)
            return count <= h
        left = 1
        right = max(piles)
        ans = -1
        while left <= right:
            mid = left + (right-left)//2
            if check(mid):
                ans = mid
                right = mid-1
            else:
                left = mid+1
        return ans    