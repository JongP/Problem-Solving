import sys
input=lambda : sys.stdin.readline().rstrip()

ansL=[]


class Trie:
    def __init__(self) :
        self.trie={}

    def add(self,word) :
        trav=self.trie
        for i in range(len(word)):
            if "*" in trav:
                return False
            elif word[i] not in trav:
                trav[word[i]]={}
                trav=trav[word[i]]
            else:
                trav=trav[word[i]]
        
        if len(trav)!=0:
            return False
        trav["*"]=True

        return True

for _ in range(int(input())):
    n=int(input())
    trie=Trie()
    flag=False
    for _ in range(n):
        if flag: 
            input()
            continue # I missed this.
        if  not trie.add(input()) :
            ansL.append(False)
            flag=True
    if not flag: ansL.append(True)




[print("YES" if a else "NO") for a in ansL]


#https://www.acmicpc.net/source/7795038

import sys
read = sys.stdin.readline

for _ in range(int(read())):
	num_of_tels = int(read())
	tels = [read()[:-1] for _ in range(num_of_tels)]
	tels.sort()
	for i in range(num_of_tels - 1):
		if tels[i+1].startswith(tels[i]):
			print("NO")
			break
	else:
		print("YES")