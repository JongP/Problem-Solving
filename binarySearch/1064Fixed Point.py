class Solution:
    def fixedPoint(self, arr: List[int]) -> int:
        le,ri=0,len(arr)-1
        res=-1
        while le<=ri:
            mid=(le+ri)//2
            
            if arr[mid]==mid:
                res=mid
                ri=mid-1
            elif arr[mid]<mid:
                le=mid+1
            else:
                ri=mid-1
            
        
        
        return res