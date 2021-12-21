class Solution:
#O(n), O(n)
    def findDuplicate(self, nums: List[int]) -> int:
        mySet=set()
        for num in nums:
            if num in mySet:
                return num
            mySet.add(num)
        
        return True


#Floyd's Tortoise and Hare (Cycle Detection)  can you see the linked list in this array?
#idea from 142. Linked List Cycle II. https://leetcode.com/problems/linked-list-cycle-ii/solution/
#optimal solution
    def findDuplicate(self, nums):
        # Find the intersection point of the two runners.
        tortoise = hare = nums[0]
        while True:
            tortoise = nums[tortoise]
            hare = nums[nums[hare]]
            if tortoise == hare:
                break
        
        # Find the "entrance" to the cycle.
        tortoise = nums[0]
        while tortoise != hare:
            tortoise = nums[tortoise]
            hare = nums[hare]
        
        return hare

#various solution
#https://leetcode.com/problems/find-the-duplicate-number/discuss/705111/summary-7-solutions-%2B-consice-explanation-and-complexity-analysis

#mine
    def findDuplicate(self, nums: List[int]) -> int:
        tortoise,hare=nums[nums[0]],nums[nums[nums[0]]]
        #tortoise,hare=nums[0],nums[nums[0]] --> time limit
        #tortoise,hare=nums[0],nums[nums[nums[0]]]#--> time limit
        
        while tortoise!=hare:
            tortoise=nums[tortoise]
            hare=nums[nums[hare]]

        
        tortoise=nums[0]
        while tortoise!=hare:
            tortoise=nums[tortoise]
            hare=nums[hare]
        
        
        return hare


#bit operation
    def findDuplicate(self, nums: List[int]) -> int:
        N = len(nums) - 1
        nbits = N.bit_length()
        ans = 0
        for p in range(nbits):   # log2(N)
            mask = 1 << p
            a = sum( 1 if num & mask else 0 for num in nums )
            b = sum( 1 if num & mask else 0 for num in range(1, N+1) )
            if a > b:
                ans |= mask
        return ans