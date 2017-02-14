#Not passing all the tests

def solution(A):
    # write your code in Python 2.7
    cleanA = sorted(set(A))
    missing = min(A)

    if 1 not in cleanA:
        missing = 1
    else:
        for i in cleanA:
            if i == missing:
                missing += 1
            elif i > 0:
                break
            else:
                missing = max(A) + 1
                break

    return missing