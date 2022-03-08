class Solution:
    def simplifyPath(self, path: str) -> str:
        res=[""]
        path=path.split("/")
        
        for elem in path:
            if elem=="." or elem=="":
                continue
            elif elem=="..":
                if len(res)!=1:
                    res.pop()
            else:
                res.append(elem)
        
        return "/".join(res) if len(res)!=1 else "/"

#https://leetcode.com/problems/simplify-path/discuss/1050573/Python-Short-stack-solution-explained
class Solution:
    def simplifyPath(self, path):
        stack = []
        for elem in path.split("/"):
            if stack and elem == "..":
                stack.pop()
            elif elem not in [".", "", ".."]:
                stack.append(elem)
                
        return "/" + "/".join(stack)