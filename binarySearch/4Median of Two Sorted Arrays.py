#https://www.youtube.com/watch?v=q6IEA26hvXc
class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        if len(nums2)<len(nums1): nums1,nums2=nums2,nums1 #why?!!!!!! you should think every single code from other

        total=len(nums1)+len(nums2)
        half=total//2
        le=0 #actually you should set le to -1 to contain entire search area
        ri=len(nums1)-1
        
        while True:
            i=(le+ri)//2
            j=half-i-2
            
            left1=nums1[i] if i>=0 else -float('inf')
            right1=nums1[i+1] if i+1<len(nums1) else float('inf')
            left2=nums2[j]  if j>=0 else -float('inf')
            right2=nums2[j+1] if j+1<len(nums2) else float('inf')
            
            if left1<=right2 and left2<=right1:
                if total%2:
                    return min(right1,right2)/1
                
                return (min(right1,right2)+max(left1,left2))/2
            elif left1>right2:
                ri=i-1
            else:
                le=i+1