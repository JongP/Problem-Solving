class Solution:
    def lengthLongestPath(self, input: str) -> int:
        input="\n"+input
        l=len(input)
        stk=[]
        res=0
        idx=0
        
        while idx<l:
            #find depth
            idx+=1#on \t
            start=idx
            while idx<l and input[idx]=="\t":
                idx+=1
            
            depth= idx-start
            #parse string
            #idx on file name
            isFile=False
            nameStart=idx
            while idx+1<l and input[idx+1]!="\n":
                if input[idx]==".":
                    isFile=True
                idx+=1
            
            name=input[nameStart:idx+1]
            #idx on the right most index of file or dir name
            
            
            #update file path
            while stk and stk[-1][0]>=depth:
                stk.pop()
            stk.append((depth,name))
            
            
            #is it file
            if isFile:
                absPath="/".join( n for d,n in stk)
                #check the length
                if len(absPath)>res:
                    res=len(absPath)
            
            idx+=1
        
        
        
        
        
        return res

#https://leetcode.com/problems/longest-absolute-file-path/discuss/86619/Simple-Python-solution
def lengthLongestPath(self, input):
    maxlen = 0
    pathlen = {0: 0}
    for line in input.splitlines():
        name = line.lstrip('\t')
        depth = len(line) - len(name)
        if '.' in name:
            maxlen = max(maxlen, pathlen[depth] + len(name))
        else:
            pathlen[depth + 1] = pathlen[depth] + len(name) + 1
    return maxlen