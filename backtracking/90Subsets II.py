#similiar with permutation2 neetcode
class Solution:
    def subsetsWithDup(self, nums: List[int]) -> List[List[int]]:
        counter=collections.Counter(nums)
        res=[]
        
        
        def helper(counter,path,res):
            if not counter:
                res.append(path.copy())
                return
            
            key,val=counter.popitem()
            
            for i in range(val+1):
                
                helper(counter,path,res)
                path.append(key)
            
            for i in range(val+1): path.pop()
                
            counter[key]=val
            
            
            
        
        
        helper(counter,[],res)
        
        return res


#https://leetcode.com/problems/subsets-ii/discuss/1380237/C%2B%2BPython-Bitmasking-Backtracking-Iterative-Solutions-with-Picture-Clean-and-Concise