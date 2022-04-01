class Solution:
    
    #evaluated time complexity wrong in first time
    def splitArray(self, nums: List[int], m: int ) -> int:
        
        
        @functools.lru_cache()    
        def helper(m,idx):
            if m==1:
                return sum(nums[idx:])


            minVal=math.inf
            curTotal=0
            for i in range(idx,len(nums)-m+1):
                curTotal+=nums[i]

                val=helper(m-1,i+1)

                if minVal>max(val,curTotal):
                    minVal=max(val,curTotal)


            return minVal
        
        return helper(m,0)

from heapq import heappush,heappop


class Solution:
    
    def splitArray(self, nums: List[int], m: int ) -> int:
        le=max(nums)
        ri=sum(nums)
        res=ri
        
        while le<=ri:
            mid=(le+ri)//2
            
            if self.canSplit(nums,m,mid):
                res=mid
                ri=mid-1
            else:
                le=mid+1
                
        
        
        
        
        return res
        
        
        
    def canSplit(self,nums,m,total):
        idx=0
        #print(total)
        cur=0
        while idx<len(nums) and m>=0:
            if cur+nums[idx]>total:
                cur=nums[idx]
                m-=1
            else:
                cur+=nums[idx]
            
            
            idx+=1
        
        #print(cur,idx)
            
        
        return m>0 and cur<=total and idx==len(nums)
        
        
        
        
        
        
#https://leetcode.com/problems/split-array-largest-sum/discuss/1347821/Python-2-approaches%3A-DP-Binary-Search-Clean-and-Concise

class Solution:
    def splitArray(self, nums: List[int], m: int) -> int:
        def canPartition(largestSum):
            groups = 1
            curSum = 0
            for num in nums:
                curSum += num
                if curSum > largestSum:
                    groups += 1
                    curSum = num
            return groups <= m

        left = max(nums)
        right = sum(nums)
        ans = right
        while left <= right:
            mid = left + (right - left) // 2
            if canPartition(mid):
                ans = mid
                right = mid - 1
            else:
                left = mid + 1
        return ans
        