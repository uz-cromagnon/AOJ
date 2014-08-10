r,c = map(int, raw_input().split())
sheet = []
 
for i in xrange(0,r):
    sheet.append(map(int, raw_input().split()))
 
total = [0] * (c+1)
 
for line in sheet:
    sum = 0
    for i,tmp in enumerate(line):
        total[i] += tmp
        sum += tmp
    total[-1] += sum
    print " ".join(map(str,line)) + " " + str(sum)
print " ".join(map(str,total))