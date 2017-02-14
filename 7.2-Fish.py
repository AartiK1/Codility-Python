
#Wrong - 75%
def solution(A, B):
    # write your code in Python 2.7
    survived = 0
    
    for i in xrange(len(A)-1):
        
        if B[i] == 1 and B[i+1] == 0:
            if A[i] > A[i+1]:
                A[i+1] = A[i]
                B[i+1] = B[i]
                
        
        else: 
            survived += 1
          
    return survived + 1