
#time issue
def solution(S, P, Q):
    # write your code in Python 2.7
    impactVal = {'A': '1', 'C': '2', 'G': '3', 'T': '4'}
    
    newS = [impactVal[key] for key in S if key in impactVal]
    
    
    impacts = []
    
    for k in xrange(len(P)):
        if P[k] == Q[k]:
            impacts.append(int(newS[P[k]]))
        else:
            impacts.append(int(min(newS[P[k]:Q[k]+1])))
    return impacts    
        