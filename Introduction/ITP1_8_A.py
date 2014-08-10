import sys

input_string = sys.stdin.read()

for x in input_string:
	if x.islower():
		sys.stdout.write(x.upper())
	else:
		sys.stdout.write(x.lower())