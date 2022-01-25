#struggled. own main idea but hint from glimpse of below solution
from heapq import heappush, heappop

class HeapSet:
    def __init__(self):
        self.heap=[]
        self.set=set()
        
    def append(self,item):
        if item in self.set: return
        self.set.add(item)
        heappush(self.heap,item)
    
    def pop(self):
        val=heappop(self.heap)
        self.set.remove(val)
        return val
    
    def head(self):
        return self.heap[0] if self.heap else None

class DinnerPlates:

    def __init__(self, capacity: int):
        self.stk=[[]]
        self.leftHeap=HeapSet()
        self.leftHeap.append(0)
        
        self.cap=capacity

    def push(self, val: int) -> None:
        tStk=self.leftHeap.head()
        #print(tStk)
        self.stk[tStk].append(val)
        
        if len(self.stk[tStk])==self.cap:
            self.leftHeap.pop()
            
            if self.leftHeap.head()==None or self.leftHeap.head()+1>len(self.stk):
                self.leftHeap.append(len(self.stk))
                self.stk.append([])

    def pop(self) -> int:
        while self.stk and len(self.stk[-1])==0:
            self.stk.pop()
        if not self.stk:
            self.stk.append([])
            self.leftHeap.append(0)
            return -1
        
        self.leftHeap.append(len(self.stk)-1)
        return self.stk[-1].pop()


        
        

    def popAtStack(self, index: int) -> int:
        if len(self.stk)<=index or not self.stk[index]:
            return -1
        
        self.leftHeap.append(index)
        
        return self.stk[index].pop()
        


#https://leetcode.com/problems/dinner-plate-stacks/discuss/366331/C%2B%2BPython-Two-Solutions
class DinnerPlates:
    def __init__(self, capacity):
        self.c = capacity
        self.q = [] # record the available stack, will use heap to quickly find the smallest available stack
        # if you are Java or C++ users, tree map is another good option.
        self.stacks = [] # record values of all stack of plates, its last nonempty stack are the rightmost position

    def push(self, val):
        # To push, we need to find the leftmost available position
        # first, let's remove any stacks on the left that are full
        # 1) self.q: if there is still available stack to insert plate
        # 2) self.q[0] < len(self.stacks): the leftmost available index self.q[0] is smaller than the current size of the stacks
        # 3) len(self.stacks[self.q[0]]) == self.c: the stack has reached full capacity
        while self.q and self.q[0] < len(self.stacks) and len(self.stacks[self.q[0]]) == self.c:
            # we remove the filled stack from the queue of available stacks
            heapq.heappop(self.q)

        # now we reach the leftmost available stack to insert

        # if the q is empty, meaning there are no more available stacks
        if not self.q:
            # open up a new stack to insert
            heapq.heappush(self.q, len(self.stacks))

        # for the newly added stack, add a new stack to self.stacks accordingly
        if self.q[0] == len(self.stacks):
            self.stacks.append([])

        # append the value to the leftmost available stack
        self.stacks[self.q[0]].append(val)

    def pop(self):
        # To pop, we need to find the rightmost nonempty stack
        # 1) stacks is not empty (self.stacks) and
        # 2) the last stack is empty
        while self.stacks and not self.stacks[-1]:
            # we throw away the last empty stack, because we can't pop from it
            self.stacks.pop()

        # now we reach the rightmost nonempty stack

        # we pop the plate from the last nonempty stack of self.stacks by using popAtStack function
        return self.popAtStack(len(self.stacks) - 1)

    def popAtStack(self, index):
        # To pop from an stack of given index, we need to make sure that it is not empty
        # 1) the index for inserting is valid and，
        # 2) the stack of interest is not empty
        if 0 <= index < len(self.stacks) and self.stacks[index]:
            # we add the index into the available stack
            heapq.heappush(self.q, index)
            # take the top plate, pop it and return its value
            return self.stacks[index].pop()

        # otherwise, return -1 because we can't pop any plate
        return -1