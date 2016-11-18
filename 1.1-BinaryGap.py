"""
A binary gap within a positive integer N is any maximal sequence of consecutive zeros that is surrounded by ones at both ends in the binary representation of N.

For example, number 9 has binary representation 1001 and contains a binary gap of length 2. The number 529 has binary representation 1000010001 and contains two binary gaps: one of length 4 and one of length 3. The number 20 has binary representation 10100 and contains one binary gap of length 1. The number 15 has binary representation 1111 and has no binary gaps.

Write a function:

def solution(N)
that, given a positive integer N, returns the length of its longest binary gap. The function should return 0 if N doesn't contain a binary gap.

For example, given N = 1041 the function should return 5, because N has binary representation 10000010001 and so its longest binary gap is of length 5.

Assume that:

N is an integer within the range [1..2,147,483,647].
Complexity:

expected worst-case time complexity is O(log(N));
expected worst-case space complexity is O(1).
"""
def solution(N):
    # write your code in Python 2.7
    #Turn int to binary list
    binary = bin(N)[2:]
    #store all the binary gap lengths here
    binary_gap_lengths = []
    #consecutive gap count
    gap_count = 0
    for i in binary:
        #if i=0, add 1 to gap count
        if i == '0':
            gap_count += 1
        #if i=1 and gap count is greater than 0 
        #i.e. the binary gap has just ended
        if gap_count > 0 and i == '1':
            #Add the gap count to the binary_gap_lengths list
            binary_gap_lengths.append(gap_count)
            #then reset the gap count
            gap_count = 0
    #if the binary_gap_lengths list is empty 
    #i.e no binary gaps
    #return 0
    if not binary_gap_lengths:
        return 0
    #if there are binary gaps, return the maximum gap length from the binary_gap_lengths list
    else:
        return max(binary_gap_lengths)