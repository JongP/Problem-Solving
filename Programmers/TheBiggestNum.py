def solution(numbers):
    l = len(numbers)
    numbers = list(map(str,numbers))
    numbers.sort(reverse=True)
    
    for i in range(1,l):
        j=i
        while j!=0 and numbers[j-1]+numbers[j] < numbers[j]+numbers[j-1]:
            tmp=numbers[j-1]
            numbers[j-1]= numbers[j]
            numbers[j]=tmp
            j-=1
            
    return str(int("".join(numbers))) #last corner case