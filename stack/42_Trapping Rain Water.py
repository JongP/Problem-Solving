class Solution:
    def trap(self, height: List[int]) -> int:
        res=0
        stk=[]
        for i,h in enumerate(height):
            grd=-1
            while stk and height[stk[-1]]<h:
                if grd==-1:
                    grd=height[stk.pop()]
                    continue
                tmpI=stk.pop()
                tmpH=height[tmpI]
                res+=(tmpH-grd)*(i-tmpI-1)
                grd=tmpH
            
            if grd!=-1 and stk and height[stk[-1]]>=h:
                res+=(h-grd)*(i-stk[-1]-1)
                
            #print(i,h,res)   
            stk.append(i)
            
        return res