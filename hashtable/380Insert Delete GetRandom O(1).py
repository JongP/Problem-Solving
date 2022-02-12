from random import randrange

class RandomizedSet:

    def __init__(self):
        self.data={}
        self.listSet={}
        self.size=0
        

    def insert(self, val: int) -> bool:
        if val in self.data:
            return False
        
        self.data[val]=self.size
        self.listSet[self.size]=val
        self.size+=1
        return True
        
    def remove(self, val: int) -> bool:
        if val not in self.data: return False
        
        idx=self.data[val]
        
        self.size-=1
        newVal=self.listSet[self.size]
        self.listSet[idx]=newVal
        self.data[newVal]=idx
        
        del self.listSet[self.size]
        del self.data[val]
        
        return True

    def getRandom(self) -> int:
        idx=randrange(self.size)
        return self.listSet[idx]
        
#https://leetcode.com/problems/insert-delete-getrandom-o1/discuss/85397/Simple-solution-in-Python
import random

class RandomizedSet(object):

    def __init__(self):
        self.nums, self.pos = [], {}
        
    def insert(self, val):
        if val not in self.pos:
            self.nums.append(val)
            self.pos[val] = len(self.nums) - 1
            return True
        return False
        

    def remove(self, val):
        if val in self.pos:
            idx, last = self.pos[val], self.nums[-1]
            self.nums[idx], self.pos[last] = last, idx
            self.nums.pop(); self.pos.pop(val, 0)
            return True
        return False
            
    def getRandom(self):
        return self.nums[random.randint(0, len(self.nums) - 1)]
