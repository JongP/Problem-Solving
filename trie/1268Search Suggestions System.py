class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        ALPHA="abcdefghijklmnopqrstuvwxyz"
        trie=self.buildTrie(products)
        startNode,startWord=trie,[]
        flag=False
        res=[]
        
        
        
        
        
        def makeList(node,res,path):
            
            if "*" in node:
                res.append("".join(path))
            
      
            
            for c in sorted(node.keys()):
                if c =="*":continue
                    
                if len(res)==3: return
                path.append(c)
                makeList(node[c],res,path)
                path.pop()
                    
                    
            
            
        
        for c in searchWord:
            if flag or c not in startNode:
                flag=True
                res.append([])
                continue
                
            startNode=startNode[c]
            startWord.append(c)
            
            tmpL=[]
            makeList(startNode,tmpL,startWord)
            res.append(tmpL)
            
        
        
        return res
            
        
        
        
    def buildTrie(self,products):
        ret={}
        
        for word in products:
            trav=ret
            for c in word:
                if c not in trav: trav[c]={}
                trav=trav[c]
            
            trav["*"]=True
            
        return ret


#https://leetcode.com/problems/search-suggestions-system/discuss/1242823/C%2B%2BPython-3-solutions-Clean-and-Concise
#optmize using sorting+ (two pointer or binary search)
class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        n = len(products)
        products.sort()  # Sort by increasing lexicographically order of products
        ans = []
        startIdx, endIdx = 0, n - 1
        for i, c in enumerate(searchWord):
            while startIdx <= endIdx and (i >= len(products[startIdx]) or products[startIdx][i] < c):
                startIdx += 1
            while startIdx <= endIdx and (i >= len(products[endIdx]) or products[endIdx][i] > c):
                endIdx -= 1

            if startIdx <= endIdx:
                ans.append(products[startIdx:min(startIdx+3, endIdx+1)])
            else:
                ans.append([])
        return ans

class Solution:
    def suggestedProducts(self, products: List[str], searchWord: str) -> List[List[str]]:
        n = len(products)
        products.sort()  # Sort by increasing lexicographically order of products
        ans = []
        beginSearch = 0
        prefix = ""
        for c in searchWord:
            prefix += c
            beginSearch = insertIndex = bisect_left(products, prefix, beginSearch, n)
            suggestProducts = []
            for i in range(insertIndex, min(insertIndex+3, n)):
                if products[i].startswith(prefix):
                    suggestProducts.append(products[i])
            ans.append(suggestProducts)
        return ans