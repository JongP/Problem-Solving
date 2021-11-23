class Solution:
    def dailyTemperatures(self, temperatures: List[int]) -> List[int]:
        stack=[]
        l=len(temperatures)
        answer=[0]*l
        
        for i,v in enumerate(temperatures):
            while stack and stack[-1][0]<v:
                _,curI=stack.pop()
                answer[curI]=i-curI
                
            stack.append((v,i))
                
                
        return answer