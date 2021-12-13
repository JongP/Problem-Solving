class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        stk=[]
        l=len(heights)
        ans=0
        for i,v in enumerate(heights):
            mySubI=i
            while stk and heights[stk[-1][0]]>v:
                tmpI,subI=stk.pop()
                if ans<(i-subI)*heights[tmpI]:
                    ans=(i-subI)*heights[tmpI]
                mySubI=subI
            
            if stk and heights[stk[-1][0]]==v:
                continue
            stk.append((i,mySubI))
            
        while stk:
            tmpI,subI=stk.pop()
            if ans<(l-subI)*heights[tmpI]:
                ans=(l-subI)*heights[tmpI]
        
            
        return ans
#https://leetcode.com/problems/largest-rectangle-in-histogram/discuss/452612/Thinking-Process-for-Stack-Solution