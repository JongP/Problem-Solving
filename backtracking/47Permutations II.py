class Solution:
    #not efficient solution
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        visited=[0]*len(nums)
        visitedAns=set()
        res=[]
        def backtracing(nums,ans,visited,res):
            if len(ans)==len(nums):
                tmp=tuple(ans)
                if tmp not in visitedAns:
                    visitedAns.add(tmp)
                    res.append(ans.copy())
                return 
            
            
            for i in range(len(nums)):
                if visited[i]: continue
                visited[i]=1
                ans.append(nums[i])
                backtracing(nums,ans,visited,res)
                ans.pop()
                visited[i]=0
        
        backtracing(nums,[],visited,res)
        
        return res

    #main idea from ctci
    def permuteUnique(self, nums: List[int]) -> List[List[int]]:
        dic={}
        for num in nums:
            dic[num]=dic.get(num,0)+1
        res=[]
        
        
        def btr(nums,dic,res,path):
            if len(path)==len(nums):
                res.append(path.copy())
                
            for key in dic:
                if dic[key]==0:continue
                dic[key]-=1
                
                path.append(key)
                btr(nums,dic,res,path)
                path.pop()
                dic[key]+=1

        btr(nums,dic,res,[])    
            
        return res