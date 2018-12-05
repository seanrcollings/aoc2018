# Part 1: 
from collections import Counter
input_file = open('puzzleinputday2.py', 'r')
input_data = [x.rstrip('\n') for x in input_file.readlines()]

repeats2 = 0
repeats3 = 0

for line in input_data: 
	hash_line = Counter(line)
	used2 = False
	used3 = False
	for key, value in hash_line.items():
		if value == 2 and not used2:
			used2 = True
			repeats2 += 1
		if value == 3 and not used3:
			used3 = True
			repeats3 +=1

print('Part 1 answer: ' + str(repeats2 * repeats3))
# Part 1 answer: 7410

# Part 2:
from difflib import SequenceMatcher

def find_dif(id1, id2):
	if SequenceMatcher(None, id1, id2).ratio() == 0.9615384615384616: # this is terrible
		print(id1 + ' ' + id2)

input_hash = {}

for line in input_data:
	for num in range(len(line) - 1):
		removed_char = line[:num] + line[num + 1:]
		if removed_char in input_hash:
			find_dif(line, input_hash[removed_char])
		else:
			input_hash.update({removed_char: line})

input_file.close()


