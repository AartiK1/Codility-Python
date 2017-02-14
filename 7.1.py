# you can write to stdout for debugging purposes, e.g.
# print "this is a debug message"

#need to fix

def solution(S):
    sol = 0
    # write your code in Python 2.7
    matched = { "[" : "]", "{" : "}", "(" : ")" }
    if S == "":
        return 1
    elif len(S)%2 == 1:
        return 0
        
    elif 
        for i in xrange(len(S)/2):
            #if odd
            if (len(S)/2)%2 == 1: 
            
            if matched[S[i]] == S[(-1 * i)-1]:
                sol += 1   
            if sol == len(S)/2:
                return 1
            else:
                return 0 
    
    else:
        for j in xrange(len(S)/2):
            if matched[S[(-1 * j)-1]] == S[j]:
                sol += 1
                print j, S[(-1 * j)-1]
            if sol == len(S)/2:
                return 1
            else:
                return 0 