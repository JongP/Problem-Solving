class Solution:
    def longestPrefix(self, s: str) -> str:
        MOD=10**9+7
        prefix=0
        surfix=0
        cur=-1
        
        for i in range(len(s)-1):
            j=len(s)-1-i
            
            prefix=(26*prefix+ord(s[i])-ord('a'))%MOD
            # surfix=(surfix+(ord(s[j])-ord('a'))*pow(26,i,MOD))%MOD #missed line
            surfix=(surfix+(ord(s[j])-ord('a'))*powNum)%MOD
            powNum=(powNum*26)%MOD
            
            if prefix==surfix:
                cur=i
        
        
        
        return s[:cur+1]

#https://leetcode.com/problems/longest-happy-prefix/discuss/547237/JavaPython-Rolling-Hash
    def longestPrefix(self, s):
        # res stores the index of the end of the prefix, used for output the result
        # l stores the hash key for prefix
        # r stores the hash key for suffix
        # mod is used to make sure that the hash value doesn't get too big, you can choose another mod value if you want.
        res, l, r, mod = 0, 0, 0, 10**9 + 7

        # now we start from the beginning and the end of the string
        # note you shouldn't search the whole string! because the longest prefix and suffix is the string itself
        for i in range(len(s) - 1):

            # based on an idea that is similar to prefix sum, we calculate the prefix hash in O(1) time.
            # specifically, we multiply the current prefix by 128 (which is the length of ASCII, but you can use another value as well)
            # then add in the ASCII value of the upcoming letter
            l = (l * 128 + ord(s[i])) % mod

            # similarly, we can calculate the suffix hash in O(1) time.
            # Specifically, we get the ith letter from the end using s[~i], note ~i is -i-1
            # we find the pow(128, i, mod) and multiply by the letter's ASCII value
            # Actually, if we don't care about the beautifulness of the code, you can have a variable to keep track of pow(128, i, mod) as you increase i
            r = (r + pow(128, i, mod) * ord(s[~i])) % mod

           # we check if the prefix and suffix agrees, if yes, we find yet another longer prefix, so we record the index
            if l == r: res = i + 1

       # after we finish searching the string, output the prefix
        return s[:res]



#KMP solution
#https://leetcode.com/problems/longest-happy-prefix/discuss/553594/Java-6-lines-KMP-Solution-Clean-code-O(N)
class Solution {
    public String longestPrefix(String s) {
        int n = s.length();
        int[] lps = new int[n];
        for (int i = 1, j = 0; i < n; i++) {
            while (j > 0 && s.charAt(i) != s.charAt(j)) j = lps[j-1];
            if (s.charAt(i) == s.charAt(j)) lps[i] = ++j;
        }
        return s.substring(0, lps[n-1]);
    }
}