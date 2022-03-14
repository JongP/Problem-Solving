#hint 2
class Solution:
    def maxArea(self, height: List[int]) -> int:
        res=0
        
        le,ri=0,len(height)-1
        
        while le+1<ri:
            #print(le,ri,height[le],height[ri])
            cur=min(height[le],height[ri])*(ri-le)
            if cur>res: res=cur
                
            
            if height[le]<height[ri]:
                le+=1
            elif height[le]>height[ri]:
                ri-=1
            else:
                le+=1
                ri-=1
                
                
                
        cur=min(height[le],height[ri])*(ri-le)
        if cur>res: res=cur
        
        
        return res

#leetcode
public class Solution {
    public int maxArea(int[] height) {
        int maxarea = 0, l = 0, r = height.length - 1;
        while (l < r) {
            maxarea = Math.max(maxarea, Math.min(height[l], height[r]) * (r - l));
            if (height[l] < height[r])
                l++;
            else
                r--;
        }
        return maxarea;
    }
}

#https://leetcode.com/problems/container-with-most-water/discuss/6100/Simple-and-clear-proofexplanation
# Idea / Proof:

# The widest container (using first and last line) is a good candidate, because of its width. Its water level is the height of the smaller one of first and last line.
# All other containers are less wide and thus would need a higher water level in order to hold more water.
# The smaller one of first and last line doesn't support a higher water level and can thus be safely removed from further consideration.
