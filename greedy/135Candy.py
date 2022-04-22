class Solution:
    def candy(self, ratings: List[int]) -> int:
        """
        keep monotonic increasing stk [(val,minimum Candy)]
        1 2 3 4 5 4 3 2 2 3
        
        """
        l=len(ratings)
        
        leftStk=[1]
        
        for i in range(1,l):
            if ratings[i-1]<ratings[i]:
                leftStk.append(leftStk[-1]+1)
            else:
                leftStk.append(1)
                
                
        rightStk=[1]
        for i in range(l-2,-1,-1):
            if ratings[i]>ratings[i+1]:
                rightStk.append(rightStk[-1]+1)
            else:
                rightStk.append(1)
            
        rightStk.reverse()

        
        return sum(max(leftStk[i],rightStk[i]) for i in range(l))