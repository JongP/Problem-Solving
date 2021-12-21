class Solution:
#O(2^n)
    def generateParenthesis(self, n: int) -> List[str]:
        res=[]
        def helper(le,ri,path):
            
            
            if le==0:
                res.append(path+(")"*ri))
                return
            elif ri==0:
                res.append(path+("("*le))
                return
            
            
            helper(le-1,ri,path+"(")
            if le<ri:
                helper(le,ri-1,path+")")
        
        
        helper(n,n,"")
        
        return res


#https://leetcode.com/problems/generate-parentheses/discuss/215927/Python-solution
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        def generate(S, open_count, close_count):
            if len(S) == 2*n:
                res.append(S)
            if open_count < close_count:
                return 
            if open_count < n:
                generate(S+"(", open_count+1, close_count)
            if open_count > close_count:
                generate(S+")", open_count, close_count+1) 
            
        res = []
        generate("", 0, 0)
        return res
    