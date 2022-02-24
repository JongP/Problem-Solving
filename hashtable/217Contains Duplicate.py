class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(nums)!=len(set(nums))
        hashMap=set()
        
        for num in nums:
            if num in hashMap: return True
            hashMap.add(num)
        
        return False