class Solution:
    def countBinarySubstrings(self, s: str) -> int:
        cnt=0
        res=0
        idx=0
        
        while idx<len(s):
            cur=s[idx]
            tmpCnt=0
            while idx<len(s) and cur==s[idx]: 
                idx+=1
                tmpCnt+=1
            
            res+=min(tmpCnt,cnt)
            
            cnt=tmpCnt

        
        return res
            
#https://leetcode.com/problems/count-binary-substrings/discuss/108625/JavaC%2B%2BPython-Easy-and-Concise-with-Explanation
    int countBinarySubstrings(string s) {
        int cur = 1, pre = 0, res = 0;
        for (int i = 1; i < s.size(); i++) {
            if (s[i] == s[i - 1]) cur++;
            else {
                res += min(cur, pre);
                pre = cur;
                cur = 1;
            }
        }
        return res + min(cur, pre);
    }