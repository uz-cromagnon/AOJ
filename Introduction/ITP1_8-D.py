s = raw_input()
p = raw_input()

ring_str = s*2

if ring_str.find(p) > -1:
	print 'Yes'
else:
	print 'No'
	
