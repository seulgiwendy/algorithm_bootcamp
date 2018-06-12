def insert(A):
    for i in range(1, len(A)):
        print("start index : ", i)
        for j in range(i, 0, -1):
            print("comparison: ", A[j], "target: ", A[j - 1])
            if A[j] < A[j-1]:
                print("switch started")
                A[j], A[j-1] = A[j-1], A[j]
            else: break
    return A

print(insert([1, 3, 2, 5, 4, 10, 11, 8, 7, 101, 6]))
