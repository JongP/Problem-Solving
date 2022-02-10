from collections import deque
class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        res=[]
        db=self.initInput(cpdomains)
#        print(db)
        self.getResult(db,res)

        
        return res
    
    def initInput(self,cpdomains):
        res={}
        
        
        
        for elem in cpdomains:
            rep,domain=elem.split();
            rep=int(rep)
            domain=domain.split(".")
            #print(rep,domain)
            
            trav=res
            while domain:
                cur=domain.pop()
                if cur not in trav:
                    trav[cur]={"*":0}
                trav=trav[cur]
                trav["*"]+=rep
                
        return res
    
    def getResult(self,db,res):
        
        def getString(path,rep):
            return " ".join([str(rep),".".join(path)])
        
        def helper(trav,path,res):
            
            for key in trav:
                if key=="*": continue
                path.appendleft(key)
                #print(key)
                rep=trav[key]["*"]
                res.append(getString(path,rep))
                helper(trav[key],path,res)
                path.popleft()
                
        
        helper(db,deque(),res)
    
#https://leetcode.com/problems/subdomain-visit-count/discuss/121738/C%2B%2BJavaPython-Easy-Understood-Solution
    def subdomainVisits(self, cpdomains):
            count = collections.Counter()
            for cd in cpdomains:
                n, s = cd.split()
                count[s] += int(n)
                for i in range(len(s)):
                    if s[i] == '.':
                        count[s[i + 1:]] += int(n)
            return ["%d %s" % (count[k], k) for k in count]