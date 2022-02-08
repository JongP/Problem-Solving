class Solution:
    def minTaps(self, n: int, ranges: List[int]) -> int:
        idx=-1
        dp=[0]*(n+1)
        
        for i,r in enumerate(ranges):
            s,e= i-r if i-r>=0 else 0,i+r
            if dp[s]<e: 
                dp[s]=e

            
        
        reach=dp[0]
        if reach>=n: return 1
        tmpReach=dp[0]
        res=1
        idx=0
        
        while idx<=reach and idx<len(dp):
            
            if dp[idx]>tmpReach: tmpReach=dp[idx]
            
            if idx==reach:
                reach=tmpReach
                res+=1
                if reach>=n:
                    return res
                
            idx+=1
        
        return  -1
#jump game
#https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/discuss/484341/Python-Jump-Game-II
    def minTaps(self, n: int, ranges: List[int]) -> int:
        max_range = [0] * (n + 1)
        
        for i, r in enumerate(ranges):
            left, right = max(0, i - r), min(n, i + r)
            max_range[left] = max(max_range[left], right - left)
        
		# it's a jump game now
        start = end = step = 0
        
        while end < n:
            step += 1
            start, end = end, max(i + max_range[i] for i in range(start, end + 1))
            if start == end:
                return -1
            
        return step

#dp solution
#https://leetcode.com/problems/minimum-number-of-taps-to-open-to-water-a-garden/discuss/484235/JavaC%2B%2BPython-Similar-to-LC1024
    def minTaps(self, n, A):
        dp = [0] + [n + 2] * n
        for i, x in enumerate(A):
            for j in xrange(max(i - x + 1, 0), min(i + x, n) + 1):
                dp[j] = min(dp[j], dp[max(0, i - x)] + 1)
        return dp[n] if dp[n] < n + 2 else -1
"""
class Solution {
public:
    int minTaps(int n, vector<int>& r) {
        
        // dp[i] is the min number of tapes to water area from 0 to i
        vector<int> dp(n+1,n+2); // Initialize with max 
        dp[0] = 0;               // minimum tapes needed to water area 0 is 0(basically no area)
        for(int i=0;i<=n;i++)  
        {
            int left = max(0,i-r[i]);     // find the minimum point of garden(area) to water with tape i.
            int right = min(n,i+r[i]);       // find the maximum point of garden(area) to water with tape i.
            for(int j=left+1;j<=right;j++)   
            {                
                //Check if this range from(left..right) can be watered using less number of tapes than previous
                dp[j] = min(dp[j], dp[left]+1); 
            }
        }
        
        // If mimimum tapes needed to water area 0..n is greater than n , it means we could not found minimum number of tapes
        if(dp[n]>=n+2)   
            return -1;
        return dp[n];
    }
};
"""