import sys
input=lambda : sys.stdin.readline().rstrip()

class Trie:
    def __init__(self):
        self.trie={-1:True}
    
    def add(self,word):
        trav=self.trie
        for c in word:
            if c not in trav:
                trav[c]={-1:True}
            trav=trav[c]
        trav["*"]={-1:True}

    def setFlag(self,word):
        trav=self.trie
        trav[-1]=False
        for c in word:
            if c in trav:
                trav=trav[c]
                trav[-1]=False
            else:
                break

    def getRes(self):
        res=0
        stk=[self.trie]
        while stk:
            cur=stk.pop()
            if cur[-1]:
                res+=1
            else:
                for nextt in cur:
                    if nextt==-1: continue
                    stk.append(cur[nextt])
        return res

ansL=[]
for _ in range(int(input())):
    trie=Trie()
    N1=int(input())
    for _ in range(N1):
        trie.add(input())

    N2=int(input())
    for _ in range(N2):
        trie.setFlag(input())

    ansL.append(trie.getRes())

[print(a) for a in ansL]