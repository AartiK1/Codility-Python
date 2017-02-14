"""
Write a function:

def solution(A, B, K)
that, given three integers A, B and K, returns the number of integers within the range [A..B] that are divisible by K, i.e.:

{ i : A ≤ i ≤ B, i mod K = 0 }
For example, for A = 6, B = 11 and K = 2, your function should return 3, because there are three numbers divisible by 2 within the range [6..11], namely 6, 8 and 10.

Assume that:

A and B are integers within the range [0..2,000,000,000];
K is an integer within the range [1..2,000,000,000];
A ≤ B.
Complexity:

expected worst-case time complexity is O(1);
expected worst-case space complexity is O(1).
"""

#Version 1 - Performance issue
def solution(A, B, K):
    # write your code in Python 2.7
    AB = range(A, B+1)
    solution = 0
        for number in AB:
            if number % K == 0:
                solution += 1
    return solution

# Version 2 - 100%

def solution(A, B, K):
    if B < A or K <= 0:
        raise Exception("Invalid Input")
        
    #Find 1st valid value bigger than A
    min_value =  ((A + K -1) // K) * K
 
    if min_value > B:
      return 0
    #If a min value within range is found
    #quantity of numbers that are divisible is 
    # the quantity of divisible numbers within range + 1 to account for the min value
    return ((B - min_value) // K) + 1
