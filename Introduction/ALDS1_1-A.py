def trace(s):
    print " ".join(map(str,s))

n = input()
A = map(int, raw_input().split())
if len(A) != n: exit()

trace(A)

for i in xrange(1, n):
    key = A[i]
    j = i - 1
    while j >= 0 and A[j] > key:
        A[j+1] = A[j]
        j -= 1
    A[j+1] = key
    trace(A)
