class Solution(object):
    def intervalIntersection(self, firstList, secondList):
        """
        :type firstList: List[List[int]]
        :type secondList: List[List[int]]
        :rtype: List[List[int]]
        """
        l1=len(firstList)
        l2=len(secondList)
        
        
        #corner case
        if l1==0 or l2==0:
            return None
        
        i=0
        j=0
        answer=[]
        
        while i<l1 and j<l2:
            if firstList[i][0]<secondList[j][0]:
                if j==0:
                    i+=1
                    continue
                
                if secondList[j-1][1]>=firstList[i][0] and secondList[j-1][0]!=firstList[i][0]:
                    answer.append([firstList[i][0],min(secondList[j-1][1],firstList[i][1])])
                
                i+=1
            elif firstList[i][0]>secondList[j][0]:
                if i==0:
                    j+=1
                    continue
                
                if firstList[i-1][1]>=secondList[j][0] and firstList[i-1][0]!=secondList[j][0]:
                    answer.append([secondList[j][0],min(firstList[i-1][1],secondList[j][1])])
                
                j+=1
            else:
                answer.append([secondList[j][0],min(firstList[i][1],secondList[j][1])])
                if firstList[i][1]>secondList[j][1]:
                    j+=1
                elif firstList[i][1]<secondList[j][1]:
                    i+=1
                else:
                    i+=1
                    j+=1
        
        while i<l1 and firstList[i][0]<=secondList[-1][1]:
            if firstList[i][0]!=secondList[-1][0]:
                answer.append([firstList[i][0],min(firstList[i][1],secondList[-1][1])])
            i+=1
        
        while j<l2 and secondList[j][0]<=firstList[-1][1]:
            if secondList[j][0]!=firstList[-1][0]:
                answer.append([secondList[j][0],min(secondList[j][1],firstList[-1][1])])
            j+=1           
        
                
        
        return answer

    def bestIntervalIntersection(self, A, B) :
        i = 0
        j = 0
         
        result = []
        while i < len(A) and j < len(B):
            a_start, a_end = A[i]
            b_start, b_end = B[j]
            if a_start <= b_end and b_start <= a_end:                       # Criss-cross lock
                result.append([max(a_start, b_start), min(a_end, b_end)])   # Squeezing
                 
            if a_end <= b_end:         # Exhausted this range in A
                i += 1               # Point to next range in A
            else:                      # Exhausted this range in B
                j += 1               # Point to next range in B
        return result