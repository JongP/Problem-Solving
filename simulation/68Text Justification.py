class Solution:
    def fullJustify(self, words: List[str], maxWidth: int) -> List[str]:
        res=[]
        stk=[]
        stkTotal=0
        
        
        def makeLine(stk,stkTotal,res):
            sNum=maxWidth-stkTotal
            l=len(stk)-1
            #print(stk,sNum,l)
            if l==0:
                res.append(stk[0]+" "*sNum) 
                stk.clear()
                return
            mul,re=divmod(sNum,l)
            tmpL=[stk[0]]
            
            for i in range(1,len(stk)):
                tmpL.append(" "*(mul + (1 if re>0 else 0)))
                tmpL.append(stk[i])
                re-=1
            
            res.append("".join(tmpL))

            stk.clear()
            
        
        def makeLastLine(stk,stkTotal,res):
            sNum=maxWidth-(stkTotal+len(stk)-1)
            
            
            res.append(" ".join(stk)+" "*sNum)
        
        
        for word in words:
            if stkTotal+len(stk)+len(word)>maxWidth:
                makeLine(stk,stkTotal,res)
                stkTotal=0
            
            stkTotal+=len(word)
            stk.append(word)
        
        makeLastLine(stk,stkTotal,res)
        
        
        return res



#https://leetcode.com/problems/text-justification/discuss/24891/Concise-python-solution-10-lines.
    def fullJustify(self, words, maxWidth):
        res, cur, num_of_letters = [], [], 0
        for w in words:
            if num_of_letters + len(w) + len(cur) > maxWidth:
                for i in range(maxWidth - num_of_letters):
                    cur[i%(len(cur)-1 or 1)] += ' '
                res.append(''.join(cur))
                cur, num_of_letters = [], 0
            cur += [w]
            num_of_letters += len(w)
        return res + [' '.join(cur).ljust(maxWidth)]