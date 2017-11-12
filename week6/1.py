def merge(A, B):
    C = []
    i = 0
    j = 0
    while len(C) != len(A) + len(B):
        if i <= len(A) - 1 and j <= len(B) - 1:
            if A[i] <= B[j]:
                C.append(A[i])
                i += 1
            else:
                C.append(B[j])
                j += 1
        elif i > len(A) - 1:
            C.append(B[j])
            j += 1
        else:
            C.append(A[i])
            i += 1
    return C

A = list(map(int, input().split()))
B = list(map(int, input().split()))
print(*merge(A, B))
