class Solution:
    def evalRPN(self, tokens: List[str]) -> int:
        stk=[]
        
        for token in tokens:
            if token[-1].isdigit():
                stk.append(int(token))
            else:
                a=stk.pop()
                b=stk.pop()
                
                if token=="+":
                    stk.append(a+b)
                elif token=="-":
                    stk.append(b-a)
                elif token=="*":
                    stk.append(a*b)
                else:
                    stk.append(math.floor(b/a) if b/a>0 else math.ceil(b/a))
        return stk.pop()

#leetcode solution
#dict lambda solution!
def evalRPN(self, tokens: List[str]) -> int:
        
    operations = {
        "+": lambda a, b: a + b,
        "-": lambda a, b: a - b,
        "/": lambda a, b: int(a / b),
        "*": lambda a, b: a * b
    }
    
    stack = []
    for token in tokens:
        if token in operations:
            number_2 = stack.pop()
            number_1 = stack.pop()
            operation = operations[token]
            stack.append(operation(number_1, number_2))
        else:
            stack.append(int(token))
    return stack.pop()