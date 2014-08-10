S = input()
if S < 0 or S > 86400 : exit()
h = S / 3600
S %= 3600
m = S / 60
s = S % 60
print '%d:%d:%d' %(h,m,s)