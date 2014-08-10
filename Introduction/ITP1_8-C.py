import sys
 
input_string  = sys.stdin.read()
alphabet = 'abcdefghijklmnopqrstuvwxyz'

for x in alphabet:
	print x + ' : ' + str(input_string.lower().count(x))

