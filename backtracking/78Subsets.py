class Solution:
    #think again on time complexity/ recursion --> nodes of tree
    #can you come up with bit vector
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res=[]

        def makeSet(nums,path):
            res=[]

            for i in range(len(nums)):
                if (path>>i)&1: res.append(nums[i])

            return res

        
        def dfs(nums,idx,path,res):
            if idx==len(nums):
                res.append(self.makeSet(nums,path))
                return
            
            dfs(nums,idx+1,path,res)
            
            path|=1<<idx
            dfs(nums,idx+1,path,res)
            path&=1<<i
        
        
        
        dfs(nums,0,0,res)
        
        return res


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        
        if not nums: return [[]]
        
        val=nums.pop()
        
        res=self.subsets(nums)
        
        for i in range(len(res)):
            tmp=res[i].copy()
            tmp.append(val)
            res.append(tmp)
        
        
        return res


#https://leetcode.com/problems/subsets/discuss/27301/Python-easy-to-understand-solutions-(DFS-recursively-Bit-Manipulation-Iteratively).
    # Bit Manipulation    
    def subsets2(self, nums):
        res = []
        nums.sort()
        for i in xrange(1<<len(nums)):
            tmp = []
            for j in xrange(len(nums)):
                if i & 1 << j:  # if i >> j & 1:
                    tmp.append(nums[j])
            res.append(tmp)
        return res


#example solution
    def subsets(self, nums: List[int]) -> List[List[int]]:
        res = [[]]
        for n in nums:
            res += [r + [n] for r in res ]
            # for i in range(len(res)):
                # res.append(list(res[i]) + [n])
        return res