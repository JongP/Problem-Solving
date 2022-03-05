class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Do not return anything, modify nums1 in-place instead.
        """
        idx=len(nums1)-1
        idx1=m-1
        idx2=len(nums2)-1
        
        while idx>=0 and idx2>=0:
            if idx1<0 or nums1[idx1]<nums2[idx2]:
                nums1[idx],nums2[idx2] = nums2[idx2],nums1[idx]
                idx2-=1
            else:
                nums1[idx],nums1[idx1] = nums1[idx1],nums1[idx]
                idx1-=1
                
            idx-=1
        
        
            
            