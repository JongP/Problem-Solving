#unsovled
#key hint from blog below
#how to optimize trie
#https://devbelly.tistory.com/41
import sys
input=lambda : sys.stdin.readline().rstrip()

sys.setrecursionlimit(100000)


class Trie():
    def __init__(self):
        self.trie={}
        self.dp=[0]*3001
        self.dp[0]=1
        self.dp[1]=1

    def add(self,word):
        trav=self.trie
        for c in word:
            if c not in trav:
                trav[c]={}
            trav=trav[c]

        trav["*"]=True

    def getRes(self): 
        res=1
        stk=[self.trie]

        while stk:
            cur=stk.pop()

            tmp=len(cur)

            res*=self.getFac(len(cur))

            for nextt in cur:
                if nextt=="*": continue
                stk.append(cur[nextt])

        return res

    def getFac(self,n):
        if self.dp[n]==0:
           self.dp[n]=self.getFac(n-1)*n
        return self.dp[n]

def getLCP(word1,word2):
    idx=0

    while idx<len(word1) and idx<len(word2) and word1[idx]==word2[idx]: idx+=1

    return idx


trie=Trie()

words=[input() for _ in range(int(input()))]
words.sort()

prev=cur=0
for i in range(len(words)-1):
    cur=getLCP(words[i],words[i+1])+1
    trie.add(words[i][:max(prev,cur)])
    prev=cur
cur=len(words[-1])
trie.add(words[-1][:max(prev,cur)])

print(trie.getRes()%1000000007)
