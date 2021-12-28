n=int(input())

def isValid(string):
    l=len(string)
    for i in range(1,l//2+1):
        if string[-1*i:]==string[-2*i:-1*i]:
            return False
    return True

def backtracking(path,level):
    if not isValid(path):
        return
    
    if level==0:
        print(path)
        exit()

    backtracking(path+"1",level-1)
    backtracking(path+"2",level-1)
    backtracking(path+"3",level-1)
    

backtracking("",n)

#https://www.acmicpc.net/source/9042088
def is_good(seq):
    n = len(seq)
    for i in range(2, n + 1, 2):
        if seq[n - i // 2: n] == seq[n - i: n - i//2]:
            return False
    return True

N = int(input())
seq = [0]
while len(seq) <= N:
    if seq[-1] == 3:
        seq.pop()
        continue
    seq[-1] += 1
    if is_good(seq):
        seq.append(0)
        continue
seq.pop()
print(''.join([str(x) for x in seq]))

