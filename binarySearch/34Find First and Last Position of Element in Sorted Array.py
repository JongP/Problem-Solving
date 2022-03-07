class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        res = [-1,-1]
        
        
        def myBisect(isLeft):
            le,ri=0,len(nums)-1
            while le<=ri:
                mid=(le+ri)//2

                if nums[mid]<target:
                    le=mid+1
                elif nums[mid] > target:
                    ri=mid-1
                elif isLeft:
                    res[0]=mid
                    ri=mid-1
                else:
                    res[1]=mid
                    le=mid+1
        
        myBisect(True)
        
        if res[0]==-1:
            return res
        
        myBisect(False)
                
        return res
    