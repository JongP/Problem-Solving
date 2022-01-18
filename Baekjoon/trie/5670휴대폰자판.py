import sys
input=lambda : sys.stdin.readline().rstrip()
sys.setrecursionlimit(10**6)



ansL=[]

class Trie():

    def __init__(self):
        self.trie={}
        self.count=0

    def add(self,word):
        self.count+=1
        trav=self.trie
        for c in word:
            if c not in trav:
                trav[c]={}
            trav=trav[c]
        trav["*"]=set()

    def getAVG(self):
        self.total=0

        def trav(node,val):
            if "*" in node:
                self.total+=val#self not global 
            
            if len(node)>1:
                val+=1

            for nextt in node:
                trav(node[nextt],val)




        for node in self.trie:
            trav(self.trie[node],1)
        
        return round(self.total/self.count,2)



while True:
    try:n=int(sys.stdin.readline())
    except: break
    trie=Trie()
    for _ in range(n):
        trie.add(input())
    ansL.append(trie.getAVG())

[print("%.2f" %a) for a in ansL]