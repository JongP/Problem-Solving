#https://leetcode.com/problems/remove-invalid-parentheses/discuss/606847/JavaPython-DFS-with-Memoization-Fastest-Clean-and-Concise
class Solution:  # 40 ms, faster than 93.29%
    def removeInvalidParentheses(self, s: str) -> List[str]:
        @lru_cache(None)
        def dfs(i, nOpen):
            ans = set()
            if nOpen < 0:
                return ans  # Invalid -> return 0 result
            if i == len(s):
                if nOpen == 0: ans.add("")  # Valid -> Return 1 result (empty string)
                return ans

            if s[i] == '(' or s[i] == ')':  # Case 1: Skip s[i]: '(', ')'
                ans.update(dfs(i + 1, nOpen))

            if s[i] == '(':
                nOpen += 1
            elif s[i] == ')':
                nOpen -= 1
            for suffix in dfs(i + 1, nOpen):  # Case 2: Include s[i]: '(', ')' or letter
                ans.add(s[i] + suffix)
            return ans

        validParentheses = dfs(0, 0)
        maxLen = max(map(len, validParentheses))
        return filter(lambda x: len(x) == maxLen, validParentheses)