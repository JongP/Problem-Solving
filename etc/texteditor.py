def solution(operations):
    clipboard=[]
    cursor=0
    selected=(-1,-1)
    text=""
    
    
    for op in operations:
        #print(op)
        if op[0]=="T":
            word = op[5:]
            left,right=selected
            
            if left!=-1:
                front = text[:left]
                text=front+word+text[right+1:]
                cursor=len(front)+len(word)
            
            else:
                front=text[:cursor] 
                text= front +word + text[cursor:]
                cursor=len(front)+len(word)
            selected=(-1,-1)
            
        elif op[0]=="S":
            selected= tuple(map(int,op.split()[1:]))
            #print(selected)
            cursor=selected[1]+1  
            
        elif op[0]=="M":
            selected=(-1,-1)
            offset= int(op.split()[1])
            cursor = max(0, min ( cursor+offset,len(text)))
        elif op[0]=="C":
            if selected[0]==-1:
                continue
            clipboard.append(text[selected[0]:selected[1]+1])
        elif op[0]=="P":
            op=op.split()
            
            if len(op)==1:
                num=1
            else:
                num = int(op[-1])
        
            if num>len(clipboard):
                continue
                
            left,right=selected
            word= clipboard[-num]
            
            if left!=-1:
                front = text[:left]
                cursor=len(front)+len(word)
                text= front + word + text[right+1:]
                
            else:
                #print("flag")
                front = text[:cursor]
                text=front+word+text[cursor:]
                cursor = len(front) + len(word)
                #print(cursor,front,word,text[cursor:])
                
            selected=(-1,-1)
        
        #print(text)
        #print(cursor,selected)
            
            
            
        
    return text