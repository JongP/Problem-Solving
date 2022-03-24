#hint on main idea
"""Hey @eodien , I know this was a while ago but maybe this will still help a bit. The intuition that helped me get to this answer personally came when realizing that the best way to get to Y was from Y/2; and the best way to get to Y/2 was from Y/2/2, and to get there is from Y/2/2/2 .... I think you get the picture. It's almost a DP-like way of approaching the problem.
Without this first quantum leap, I think it's really damn tough to get such a concise answer"""
class Solution:
    
    def brokenCalc(self, startValue: int, target: int) -> int:
        step=0
        while startValue<target:
            if target%2:
                target= (target+1)//2
                step+=2
            else:
                target//=2
                step+=1
                
        step+= startValue-target
        
        
        return step