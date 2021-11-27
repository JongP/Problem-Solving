class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        
        ans=[]
        l=len(nums)
        
        nums.sort()
        if l<=2 or nums[0]>0 or nums[-1]<0:
            return ans
        
        
        
        
        
        for i,v in enumerate(nums):
            if v>=0:
                zIdx=i
                break
        
        
        
        lPart=nums[:zIdx]
        rPart=nums[zIdx:]
        
        if len(rPart)>=3 and rPart[0]==0 and rPart[1]==0 and rPart[2]==0:
            ans.append([0,0,0])
         
        #print(lPart,rPart)
        
        #two from lPart
        rSet=set(rPart)
        prevL=None
        for i in range(len(lPart)):
            for j in range(i+1,len(lPart)):
                if -1*(lPart[i]+lPart[j]) in rSet:
                    ans.append([lPart[i],lPart[j],-1*(lPart[i]+lPart[j])])
        
        #two form rPart
        lSet=set(lPart)
        for i in range(len(rPart)):
            for j in range(i+1,len(rPart)):
                if -1*(rPart[i]+rPart[j]) in lSet:
                    ans.append([-1*(rPart[i]+rPart[j]),rPart[i],rPart[j]])
                    

        tmpT= (tuple(elem) for elem in ans)
        ans=list(set(tmpT))
        
        return ans

    def simpleThreeSum(self, nums):
        res = []
        nums.sort()
        for i in range(len(nums)-2):
            if i > 0 and nums[i] == nums[i-1]:
                continue
            l, r = i+1, len(nums)-1
            while l < r:
                s = nums[i] + nums[l] + nums[r]
                if s < 0:
                    l +=1 
                elif s > 0:
                    r -= 1
                else:
                    res.append((nums[i], nums[l], nums[r]))
                    while l < r and nums[l] == nums[l+1]:
                        l += 1
                    while l < r and nums[r] == nums[r-1]:
                        r -= 1
                    l += 1; r -= 1
        return res