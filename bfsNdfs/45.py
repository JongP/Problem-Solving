from collections import deque
class Solution:
    def jump(self, nums: List[int]) -> int:
        l=len(nums)
        que=deque()
        visited=set()
        
        if l==1:
            return 0
        
        
        que.append(0)
        visited.add(0)
        ans=0
        while que:
            tmpLen=len(que)
            
            for _ in range(tmpLen):
                cur=que.popleft()

                    
                if cur==l-1:
                    return ans
                
                visited.add(cur)
                
                for i in range(1,nums[cur]+1):
                    if cur+i<l and cur+i not in visited:
                        visited.add(cur+i)
                        que.append(cur+i)
            ans+=1
            
        return False
#https://leetcode.com/problems/jump-game-ii/discuss/485780/Python-O(-n-)-sol.-based-on-greedy-of-coverage.-90%2B-With-explanation
    def jump(self, nums: List[int]) -> int:
        
        size = len(nums)
        
        # destination is last index
        destination = size - 1
        
        # record of current coverage, record of last jump index
        cur_coverage, last_jump_index = 0, 0
        
        # counter for jump
        times_of_jump = 0
        
         # Quick response if start index == destination index == 0
        if size == 1:
            return 0
        
        
        # Greedy strategy: extend coverage as long as possible with lazy jump
        for i in range( 0, size):
            
            # extend current coverage as further as possible
            cur_coverage = max( cur_coverage, i + nums[i] )
            

            # forced to jump (by lazy jump) to extend coverage  
            if i == last_jump_index:
            
                # update last jump index
                last_jump_index = cur_coverage
                
                # update counter of jump by +1
                times_of_jump += 1
                
                # check if reached destination already
                if cur_coverage >= destination:
                        return times_of_jump
                
        return times_of_jump

#https://www.youtube.com/watch?v=dJ7sWiOoK7g