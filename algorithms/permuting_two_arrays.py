def twoArrays(k, A, B):
    A.sort()
    B.sort(reverse=True)
    ok = True
    for i in range(len(A)):
        if A[i] + B[i] < k:
            ok = False
            break
    return 'YES' if ok else 'NO'
