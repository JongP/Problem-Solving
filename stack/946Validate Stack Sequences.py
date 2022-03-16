class Solution:
    #O(n) O(1)
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        idx1=-1
        idx2=0
        
        for i in range(len(pushed)):
            idx1+=1
            pushed[idx1],pushed[i]=pushed[i],pushed[idx1]
            #pushed[idx1]=pushed[i] is much more simple
            
            while idx1>=0 and idx2<len(popped)  and pushed[idx1]==popped[idx2]: 
                idx1-=1
                idx2+=1
        
        return idx1==-1
        