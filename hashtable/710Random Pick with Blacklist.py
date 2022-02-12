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
    #https://leetcode.com/problems/random-pick-with-blacklist/discuss/144441/Java-Binary-Search-Solution-O(BlogB)-for-constructor-and-O(logB)-for-pick()
    private List<Interval> intervals;
    private Random r;
    private int l;

    public Solution(int N, int[] blacklist) {
        Arrays.sort(blacklist);
        intervals = new ArrayList<>();
        r = new Random();
        l = N - blacklist.length;
        int pre = 0, count = 0;
        for (int b : blacklist) {
            if (pre != b) {
                intervals.add(new Interval(pre, b - 1, count));
                count += b - pre;
            }
            pre = b + 1;
        }
        intervals.add(new Interval(pre, N - 1, count));
    }
    
    public int pick() {
        int index = r.nextInt(l);
        int low = 0, high = intervals.size() - 1;
        while (low <= high) {
            int mid = low + (high - low) / 2;
            Interval cur = intervals.get(mid);
            if (cur.preCount <= index && index < cur.preCount + cur.high - cur.low + 1) {
                return cur.low + index - cur.preCount;
            } else if (cur.preCount > index) {
                high = mid - 1;
            } else {
                low = mid + 1;
            }
        }
        return -1;
    }
}