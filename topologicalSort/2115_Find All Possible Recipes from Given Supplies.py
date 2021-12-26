from collections import defaultdict 
class Solution:
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        n=len(recipes)
        res=[]
        que=[]
        
        inDegrees=defaultdict(int)
        graph=defaultdict(set)
        
        for i in range(n):
            recipe=recipes[i]
            inDegrees[recipe]=len(ingredients[i])
            for ingredient in ingredients[i]:
                
                graph[ingredient].add(recipe)
                
        #que=supplies is OK
        for supply in supplies:
            for rec in graph[supply]:
                inDegrees[rec]-=1
                if inDegrees[rec]==0:
                    que.append(rec)
        
        
        while que:
            res.append(que.pop())
            
            for rec in graph[res[-1]]:
                inDegrees[rec]-=1
                if inDegrees[rec]==0:
                    que.append(rec)
                    
        return res

#optimal fast solution given as example       
    def findAllRecipes(self, recipes: List[str], ingredients: List[List[str]], supplies: List[str]) -> List[str]:
        adj = defaultdict(set)
        needed_for = defaultdict(set)
        for idx in range(len(recipes)):
            for ingre in ingredients[idx]:
                adj[ingre].add(recipes[idx])
                needed_for[recipes[idx]].add(ingre)
        dq = deque()
        seen = set()
        for supply in supplies:
            dq.append(supply)
            seen.add(supply)
        while dq:
            rep = dq.popleft()
            for next_rep in adj[rep]:
                needed_for[next_rep].remove(rep)
                if next_rep not in seen and len(needed_for[next_rep]) == 0:
                    dq.append(next_rep)
                    seen.add(next_rep)
        return [recipe for recipe in recipes if recipe in seen]