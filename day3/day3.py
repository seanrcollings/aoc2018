# Part 1:
import collections; import pdb
input_file = open('input.txt', 'r')

fabric = [['.' for i in range(1000)] for i in range(1000)]

def display_fabric(): # Displays the fabric as a 100 * 100 grid of dots 
	for row in fabric:
		print_row = ''
		for cell in row:
			print_row += cell
		print(print_row)

def parse_data(line):
	line = line.strip('\n').split(' ')
	dist_left = int(line[2].partition(',')[0]) - 1 # Finds the distance from the left of the fabric and 0 indexes it
	dist_top = int(line[2].split(',')[1].strip(':')) - 1 # Finds the distance from the top of the fabric and 0 indexes it 
	width = int(line[3].partition('x')[0])
	height =  int(line[3].split('x')[1])
	return line, dist_left, dist_top, width, height

def elf_claims():
	for line in input_file.readlines():
		line, dist_left, dist_top, width, height = parse_data(line)

		for num in range(height):
			current_location = dist_left
			for num in range(width):
				if fabric[dist_top][dist_left] == '.':
					fabric[dist_top][dist_left] = 'C'
					current_location+=1
				else:
					fabric[dist_top][dist_left] = 'X'
					current_location+=1
				current_location+=1
			current_location = dist_left
			dist_top+=1
	check_overlap()

def check_overlap():
	overlap = 0
	for row in fabric:
		overlap += dict(collections.Counter(row))['X']
	print(overlap)

				
elf_claims()


input_file.close()