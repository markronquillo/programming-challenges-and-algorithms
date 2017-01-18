# deepest pit array
# solution using 1 loop only


def solution(A):
    """
    We need to look for all possible triple (P, Q, R) that
    satisfies the condition given and check which is the deepest.

    We only need one loop
    Imagine if you are going to traverse a series of pits
    to look for the deepest pit. Practically you only need
    to traverse it once.
    """
    # we set 0 index as initial P value
    P = 0
    # -1 meaning they don't have any index value to hold initially
    Q = -1
    R = -1
    deepest = 0
    for i in range(1, len(A)):
        # if there are no Q values yet
        # and the current value in the array (traversed one pass)
        # is greater or equal than the previous.
        # This means that we are now going up or in a plateau
        if Q < 0 and A[i] >= A[i-1]:
            Q = i-1

        # unless we have the Q value, we cant start probing for R value
        # we check if the current is less than or equal than the previous
        # this means that we are currently going down
        # we need also to watch out on inputs where it is still going down
        # until the end of the input (i+1 == len(A)).
        if (Q >= 0 and R < 0) and (A[i] <= A[i-1] or (i+1 == len(A))):
            if A[i] <= A[i-1]:
                R = i-1
            else:
                R = i
            deepest = max(deepest, min(A[P]-A[Q], A[R]-A[Q]))
            P = i-1
            Q = -1
            R = -1
    return deepest


print solution([0,1,3,-2,0,1,0,-3,2,3])

