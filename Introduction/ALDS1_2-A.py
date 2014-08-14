def bubble_sort(A):
        count = 0
	for i in xrange(N-1):
		for j in xrange(N-1,i,-1):
                        if A[j] < A[j-1]:
                                A[j],A[j-1] = A[j-1],A[j]
                                count += 1
        print " ".join(map(str,A))
        print count

N = input()
A = map(int, raw_input().split())
bubble_sort(A)
