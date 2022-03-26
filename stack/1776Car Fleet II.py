"""
We care about the collision time of the cars in front us.
We iteratre from the last to the first car,
and we main a stack of car indices,
where their collision time is strict decreasing.
"""
class Solution:
    def getCollisionTimes(self, cars: List[List[int]]) -> List[float]:
        stk=[]
        answer=[-1.0]*len(cars)
        
        def calTime(xpos,xtime,ypos,ytime):
            return (xpos-ypos)/(ytime-xtime)
        
        def saveElem(t):
            answer[t[0]]=t[1] if t[1]!=math.inf else -1
        
        def saveStk(s):
            while s:
                saveElem(s.pop())
                
        
        for i in range(len(cars)-1,-1,-1):
            curPos,curSpeed=cars[i]
            time=math.inf
            
            if stk and cars[stk[0][0]][1]>=curSpeed:
                saveStk(stk)
                stk.clear()
            
            
            while stk:
                tPos,tSpeed=cars[stk[-1][0]]
                
                if tSpeed<curSpeed:
                    time= min(time,calTime(tPos,tSpeed,curPos,curSpeed))
                
                if time<=stk[-1][1]:
                    break
                
                saveElem(stk.pop())
                
                
            
            
            stk.append((i,time))
        
        saveStk(stk)
        return answer
        
#https://leetcode.com/problems/car-fleet-ii/discuss/1085987/JavaC%2B%2BPython-O(n)-Stack-Solution
    def getCollisionTimes(self, A):
        stack = []
        n = len(A)
        res = [-1] * n
        for i in range(n-1, -1, -1):
            p, s = A[i]
            while stack and (s <= A[stack[-1]][1] or (A[stack[-1]][0] - p) / (s - A[stack[-1]][1]) >= res[stack[-1]] > 0):
                stack.pop()
            if stack:
                res[i] = (A[stack[-1]][0] - p) / (s - A[stack[-1]][1])
            stack.append(i)
        return res