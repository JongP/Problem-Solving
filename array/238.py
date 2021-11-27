class Solution:
    def productExceptSelf(self, nums):
        tPro=1
        ans=[]
        
        zFlag=False
        
        for num in nums:
            if num==0:
                if zFlag:
                    return [0]*len(nums)
                zFlag=True
                continue
            tPro*= num
            
        for num in nums:
            if zFlag:
                if num==0:
                    ans.append(tPro)
                else:
                    ans.append(0)
                continue
            
            ans.append(tPro//num)
        
        return ans
#https://leetcode.com/problems/product-of-array-except-self/discuss/239771/Python-solution
    def zitaoProductExceptSelf(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        res = [1]*len(nums)
        lprod = 1
        rprod = 1
        for i in range(len(nums)):
            res[i] *= lprod
            lprod *= nums[i]
            res[~i] *= rprod
            print(i,~i)#(i,~i): (0,-1), (1,-2), (2,-3), (3,-4)
            rprod *= nums[~i]
        return res

    def uniqueProductExceptSelf(self, nums):
        p = 1
        n = len(nums)
        output = []
        for i in range(0,n):
            output.append(p)
            p = p * nums[i]
        p = 1
        for i in range(n-1,-1,-1):
            output[i] = output[i] * p
            p = p * nums[i]
        return output
            
sol=Solution()            
sol.zitaoProductExceptSelf([1,2,3,4])