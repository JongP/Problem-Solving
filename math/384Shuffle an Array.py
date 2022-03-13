class Solution:

    def __init__(self, nums: List[int]):
        self.nums=nums

    def reset(self) -> List[int]:
        return self.nums

    def shuffle(self) -> List[int]:
        res=[]
        l=len(self.nums)
        indexes=[i for i in range(l)]
        
        for i in range(l):
            val=random.randrange(len(indexes))
            indexes[val],indexes[-1]=indexes[-1],indexes[val]
            res.append(self.nums[indexes.pop()])
            
        return res


#Fisher-Yate Algorithm
# https://leetcode.com/problems/shuffle-an-array/discuss/1350213/Python-Fisher-Yates-algorithm-explained
class Solution:
    def __init__(self, nums):
        self.nums = nums[:]
        self.copy = nums[:]

    def reset(self):
        self.nums = self.copy[:]
        return self.nums
        
    def shuffle(self):
        n = len(self.nums)
        for i in range(n):
            j = randint(i, n - 1)
            self.nums[i], self.nums[j] = self.nums[j], self.nums[i]
        return self.nums