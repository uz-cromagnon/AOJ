def selection_sort(A):
    count = 0
    for i in xrange(N):
        min = i
        for j in xrange(i, N):
            if A[j] < A[min]:
                min = j
        if i != min:
            A[i],A[min] = A[min],A[i]
            count += 1
    print " ".join(map(str, A))
    print count

N = input()
selection_sort(map(int, raw_input().split()))
