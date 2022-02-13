#completely unsolved
#I tried Binary search instead of remapping

from random import randint

class Solution:

    def __init__(self, N: int, blacklist: List[int]):
        blacklist = set(blacklist)  #to avoid TLE
        self.N = N - len(blacklist) #to be used in pick()
        key = [x for x in blacklist if x < N-len(blacklist)]
        val = [x for x in range(N-len(blacklist), N) if x not in blacklist]
        self.mapping = dict(zip(key, val))

    def pick(self) -> int:
        i = randint(0, self.N-1)
        return self.mapping.get(i, i)

#https://leetcode.com/problems/random-pick-with-blacklist/discuss/146533/Super-Simple-Python-AC-w-Remapping
class Solution:
    def __init__(self, N, blacklist):
        blacklist = sorted(blacklist)
        self.b = set(blacklist)
        self.m = {}
        self.length = N - len(blacklist)
        j = 0
        for i in range(self.length, N):
            if i not in self.b:
                self.m[blacklist[j]] = i
                j += 1

    def pick(self):
        i = random.randint(0, self.length - 1)
        return self.m[i] if i in self.m else i

#
class Solution {
    
    class Interval {
        int low;
        int high;
        int preCount;
        Interval(int low, int high, int preCount) {
            this.low = low;
            this.high = high;
            this.preCount = preCount;
        }
    }
    
    #BINARY SEARCH
    #https://leetcode.com/problems/random-pick-with-blacklist/discuss/1665322/Python-Binary-Search
class BinarySearchSolution:

    def __init__(self, n: int, blacklist: List[int]):
        self.n = n
        self.k = n - len(blacklist)
        self.blacklist = blacklist
        self.blacklist.sort()

    def pick(self) -> int:
        p = random.randint(0, self.k - 1)
        left, right = -1, len(self.blacklist) - 1
        while left <= right:
            mid = (left + right) // 2
            x = self.blacklist[mid + 1] if mid + 1 < len(self.blacklist) else math.inf
            if x > p + mid + 1:
                right = mid - 1
            else:
                left = mid + 1
        if left == -1:
            return p
        elif left == len(self.blacklist):
            return p + len(self.blacklist)
        else: return p + left + 1