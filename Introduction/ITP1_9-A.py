import sys

count_word = raw_input().lower()
word_list = sys.stdin.read().lower().split()

count = 0

for x in word_list:
	if x == count_word:
		count += 1
	elif x == 'END_OF_TEXT':
                break
        else:
                pass
        
print count
