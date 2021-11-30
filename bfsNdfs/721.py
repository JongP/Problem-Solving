class Solution:
    def accountsMerge(self, accounts: List[List[str]]) -> List[List[str]]:
        dic={}
        userList=[]
        prev=None
        for i,account in enumerate(accounts):
            user=[account[0],set(account[1:]),i]
            #user=list([account[0],set(account[1:])])
            userList.append(user)
            #print(user,prev)
            
            for email in user[1]:
                h=hash(email)
                #print(email)
                if h not in dic:
                    dic[h]=user
                elif dic[h]!=user:#absorb
                    prevUser=dic[h]
                    #print(email,user,prevUser)
                    prevEmails=prevUser[1]
                    for prevEmail in prevEmails:
                        dic[hash(prevEmail)]=user
                    user[1]=user[1]|prevEmails
                    prevUser[1]=None
            prev=user
        #print(userList)
        ans=[]
        for name, emails,_ in userList:
            if not emails: continue
            ans.append([name]+sorted(list(emails)))
        
        return ans

#https://leetcode.com/problems/accounts-merge/discuss/176771/Python-solution
    def accountsMerge(self, accounts):
        """
        :type accounts: List[List[str]]
        :rtype: List[List[str]]
        """
        neighbor_dic = collections.defaultdict(set)
        name_dic = {}
        for lst in accounts:
            name = lst[0]
            for email in lst[1:]:
                neighbor_dic[email].add(lst[1])
                neighbor_dic[lst[1]].add(email)
                name_dic[email] = name
                   
        res = []
        seen = set()
        for key in neighbor_dic.keys():
            if key not in seen:
                seen.add(key)
                stack = [key]
                tmp = [key]
                while stack:
                    u = stack.pop()
                    for n in neighbor_dic[u]:
                        if n not in seen:
                            seen.add(n)
                            tmp.append(n)
                            stack.append(n)
                res.append([name_dic[key]]+sorted(tmp))
        return res