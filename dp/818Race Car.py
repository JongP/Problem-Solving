#poorly sovledfrom collections import deque
#O(2^(step))
class Solution:
    def racecar(self, target: int) -> int:
        if target==0: return 0
        
        step=1
        visited=set([(0,1)])
        que=deque([(0,1)])
        
        while que:            
            for _ in range(len(que)):
                pos,speed=que.popleft()
                
                "R"
                if (pos,-1*speed//abs(speed)) not in visited:
                    visited.add((pos,-1*speed//abs(speed)))
                    que.append((pos,-1*speed//abs(speed)))
                
                
                "A"
                if (pos+speed,2*speed) not in visited:
                    if pos+speed == target: return step
                    visited.add((pos+speed,2*speed))
                    que.append((pos+speed,2*speed))
                    
            step+=1

    dp = {0: 0}

#https://leetcode.com/problems/race-car/discuss/123834/JavaC%2B%2BPython-DP-solution
    def racecar(self, t):
        if t in self.dp:
            return self.dp[t]
        n = t.bit_length()
        if 2**n - 1 == t:
            self.dp[t] = n
        else:
            self.dp[t] = self.racecar(2**n - 1 - t) + n + 1
            for m in range(n - 1):
                self.dp[t] = min(self.dp[t], self.racecar(t - 2**(n - 1) + 2**m) + n + m + 1)
        return self.dp[t]


#https://leetcode.com/problems/race-car/discuss/124326/Summary-of-the-BFS-and-DP-solutions-with-intuitive-explanation
public int racecar(int target) {
    int[] dp = new int[target + 1];
    Arrays.fill(dp, 1, dp.length, -1);
    return racecar(target, dp);
}

private int racecar(int i, int[] dp) {
    if (dp[i] >= 0) {
        return dp[i];
    }
    
    dp[i] = Integer.MAX_VALUE;
    
    int m = 1, j = 1;
    
    for (; j < i; j = (1 << ++m) - 1) {
        for (int q = 0, p = 0; p < j; p = (1 << ++q) - 1) {
            dp[i] = Math.min(dp[i],  m + 1 + q + 1 + racecar(i - (j - p), dp));
        }
    }
    
    dp[i] = Math.min(dp[i], m + (i == j ? 0 : 1 + racecar(j - i, dp)));
    
    return dp[i];
}