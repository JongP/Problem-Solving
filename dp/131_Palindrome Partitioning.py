#unoptimized solution
class Solution:
    dp={"":[[]]}
    
    def partition(self, s: str) -> List[List[str]]:
        if s in self.dp:
            return self.dp[s]
        
        def isPalindrome(strt,end):
            while strt<end:
                if s[strt]!=s[end]:
                    return False
                strt+=1
                end-=1
            return True
        
        
        res=[]
        
        for i in range(len(s)):
            if isPalindrome(0,i):
                tmpL=self.partition(s[i+1:])

                for tmp in tmpL:
                    res.append([s[:i+1]]+tmp)
        
        
        self.dp[s]=res
        return res


#https://leetcode.com/problems/palindrome-partitioning/discuss/41973/Python-recursiveiterative-backtracking-solution
def partition(self, s):
    res = []
    self.dfs(s, [], res)
    return res

def dfs(self, s, path, res):
    if not s:
        res.append(path)
        return
    for i in range(1, len(s)+1):
        if self.isPal(s[:i]):
            self.dfs(s[i:], path+[s[:i]], res)
    
def isPal(self, s):
    return s == s[::-1]

#https://leetcode.com/problems/palindrome-partitioning/discuss/42100/Python-easy-to-understand-backtracking-solution
class Solution:
    def partition(self, s: str) -> List[List[str]]:
        self.output =[]
        return self.partitionHelper(s,{})
        
    def partitionHelper(self,available,dp):
        # Base Cases
        if len(available) ==1:
            return [[available]]
        if not available:
            return [[]]
        if available in dp:
            return dp[available]
        
        # Choice Tree
        res =[]
        for i in range(1,len(available)+1):
            first = available[:i] # first substring
            second = available[i:] # second substring
            if first == first[::-1]: # if first substring is a palindrome , then call the recursive function on second
                # Get the ans from below and prepend [first] to it
                result = self.partitionHelper(second,dp)
                temp =[]
                # result can be array of array i.e multiple possibilites for a subproblem
                # e.g. if recursive call is for subproblem "aab" , then ans can be ['aa,b'] and ['a','a',b]
                # so result will be [['aa,b'], ['a','a',b]]
                # prepend "first" substring to all possible solution we got from second substring recursive call and then put it in "res" variable and pass it above in the function call
                for r in result:
                    temp.append([first]+r)
                # don't do res.append(temp)
                res += temp
        dp[available] =res
        return dp[available]


#example popular solution
    def partition(self, s: str) -> List[List[str]]:
        res = []
        
        def check_palindrome(str, left, right) -> bool:
            while left < right:
                if str[left] != str[right]:
                    return False
                left, right = left + 1, right - 1
            return True
        
        def dfs(start_index, path) -> None:#by using start_index not string we can reduce time
            if start_index == len(s):
                res.append(path[:])
                return
            for i in range(start_index, len(s)):
                if not check_palindrome(s, start_index, i):
                    continue
                path.append(s[start_index:i+1])
                dfs(i+1, path)
                path.pop()#by resuing path we can reduce time
        dfs(0, [])
        return res
    # dp
        dp = [[False] * len(s) for _ in range(len(s))]
        for i in range(len(s)):
            dp[i][i] = True
        for j in range(1, len(s)):
            for i in range(j):
                is_char_equal = s[i] == s[j]
                if j - i == 1:
                    dp[i][j] = is_char_equal
                else:
                    dp[i][j] = is_char_equal and dp[i+1][j-1]
        res = []
        def dfs(start_index, path):
            if start_index == len(s):
                res.append(path[:])
                return
            for i in range(start_index, len(s)):
                if not dp[start_index][i]:
                    continue
                path.append(s[start_index: i+1])
                dfs(i+1, path)
                path.pop()
        dfs(0,[])
        return res