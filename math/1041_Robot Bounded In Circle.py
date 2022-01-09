#too much hint
#too much intuitive
#but you can proof!!!
#The robot stays in the circle if and only if (looking at the final vector) it changes direction (ie. doesn't stay pointing north), or it moves 0.
class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        cx,cy=0,0
        cd=0#NEWS 0,1,2,3
        dxdy=((0,1),(1,0),(-1,0),(0,-1))
        toLeft=[2,0,3,1]
        toRight=[1,3,0,2]
        
        
        for i in instructions:
            if i=='G':
                cx,cy=cx+dxdy[cd][0],cy+dxdy[cd][1]
            elif i=='L':
                cd=toLeft[cd]
            elif i=='R':
                cd=toRight[cd]
                
        if (cx==0 and cy==0) or cd!=0:
            return True
        else:
            return False
        
#https://leetcode.com/problems/robot-bounded-in-circle/discuss/290856/JavaC%2B%2BPython-Let-Chopper-Help-Explain
"""
People are asking for a proof. I thought my explanation above is already the proof?
If robot return origin, it will be in the circle.
If robot ends with other direction (as shown in the diagram), it will be in the circle.
Otherwise, not back to the origin, and still faces north, it will be further and further after instructions and won't be in a circle.
Isn't it a proof good enough?
"""