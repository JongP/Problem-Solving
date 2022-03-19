#hint: stack of stacks
class FreqStack:

    def __init__(self):
        self.stks=collections.defaultdict(list)
        self.curMax=0
        self.hashMap=collections.defaultdict(int)        
        

    def push(self, val: int) -> None:
        self.hashMap[val]+=1
        
        if self.curMax<self.hashMap[val]:
            self.curMax=self.hashMap[val]
        
        self.stks[self.hashMap[val]].append(val)
        

    def pop(self) -> int:
        val=self.stks[self.curMax].pop()
        self.hashMap[val]-=1
        
        if not self.stks[self.curMax]:
            self.curMax-=1
        
        return val

#https://leetcode.com/problems/maximum-frequency-stack/discuss/163435/Python-Simple-PriorityQueue
#heap solution
class FreqStack:

    def __init__(self):
        self.heap = []
        self.m = collections.defaultdict(int)
        self.counter = 0
        
    def push(self, x):
        self.m[x]+=1
        heapq.heappush(self.heap,(-self.m[x], -self.counter, x))
        self.counter+=1
    
    def pop(self):
        toBeRemoved = heapq.heappop(self.heap)
        self.m[toBeRemoved[2]]-=1
        return toBeRemoved[2]