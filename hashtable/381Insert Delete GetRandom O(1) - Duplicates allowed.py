from random import randrange
from collections import defaultdict

class RandomizedCollection:


    def __init__(self):
        self.data=defaultdict(set)
        self.myList={}
        self.size=0
        

    def insert(self, val: int) -> bool:
        res= len(self.data[val])==0
        
        self.data[val].add(self.size)
        self.myList[self.size]=val
        self.size+=1
        #print(self.data)
        return res
        
    def remove(self, val: int) -> bool:
        if len(self.data[val])==0: return False
        assert self.size>0
        
        idx=self.data[val].pop()
        
        self.size-=1
        newVal=self.myList[self.size]
        
        
        if idx!=self.size:
            self.myList[idx]=newVal
            self.data[newVal].add(idx)
        
        self.data[newVal].discard(self.size)
        del self.myList[self.size]
        #print(self.data)
        return True

    def getRandom(self) -> int:
        idx=randrange(self.size)
        return self.myList[idx]




#using random.choice
#https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/discuss/85556/Frugal-Python-code

import random

class RandomizedCollection(object):

    def __init__(self):
        self.vals, self.idxs = [], collections.defaultdict(set)
        

    def insert(self, val):
        self.vals.append(val)
        self.idxs[val].add(len(self.vals) - 1)
        return len(self.idxs[val]) == 1
        

    def remove(self, val):
        if self.idxs[val]:
            out, ins = self.idxs[val].pop(), self.vals[-1]
            self.vals[out] = ins
            if self.idxs[ins]:
                self.idxs[ins].add(out)
                self.idxs[ins].discard(len(self.vals) - 1)
            self.vals.pop()
            return True
        return False 

    def getRandom(self):
        return random.choice(self.vals)

#https://leetcode.com/problems/insert-delete-getrandom-o1-duplicates-allowed/discuss/150148/Python-solution-using-dictionary-and-set-beat-94
class RandomizedCollection(object):

    def __init__(self):
        """
        Initialize your data structure here.
        """
        self.dic = {}
        self.dic_2 = {}
        self.n = 0

    def insert(self, val):
        """
        Inserts a value to the collection. Returns true if the collection did not already contain the specified element.
        :type val: int
        :rtype: bool
        """
        flag = not val in self.dic
        if flag:self.dic[val] = set()
        self.dic[val].add(self.n)
        self.dic_2[self.n] = val
        self.n += 1
        return flag

    def remove(self, val):
        """
        Removes a value from the collection. Returns true if the collection contained the specified element.
        :type val: int
        :rtype: bool
        """
        if not val in self.dic:return False
        val_index = self.dic[val].pop()
        if not self.dic[val]:self.dic.pop(val)
        last_val = self.dic_2.pop(self.n-1)
        if val_index != self.n-1:
            self.dic[last_val].remove(self.n-1)
            self.dic[last_val].add(val_index)
            self.dic_2[val_index] = last_val
        self.n -= 1
        return True

    def getRandom(self):
        """
        Get a random element from the collection.
        :rtype: int
        """
        return self.dic_2[random.randint(0,self.n-1)]