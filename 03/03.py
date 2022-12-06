#!/bin/python

with open("input", "r") as file:
	input_data = file.readlines()


def get_char_priority(char):
	return (ord(char) - 96) if char.islower() else (ord(char) - 38)

# So this function is fucked somewhere. Sometimes the output is +1 too high...
# but I have no idea why that is
def part_one(input_data):
	total_prio = 0
	
	for line in input_data:
		middle = int(len(line)/2)	# cast to integer to use it as index
		left = line[:middle]
		right = line[middle:]
		left.replace('\n', '')
		right.replace('\n', '')	

		# Create a string '', cast left_compartment to a set to use the intersection
		# function and add the intersection to '' to make it an easily processible
		# string
		common_char = ''.join(set(left).intersection(right))
		# !!! BEWARE !!!
		# Only use the first common character. Sometimes there are multiple common
		# chars. Imho that's the challenge's fault
		common_char = common_char[0]
		if not common_char.isalpha():	# really only process letters
			continue
	
		total_prio += get_char_priority(common_char)

	return total_prio


def part_two(input_data):
	total_prio = 0

	group = ['', '', ''] # a group of elves with three rucksacks (strings)
	
	counter = 0 # the current group member, will be 0 -> 1 -> 2 -> 0 -> 1 ->...

	for line in input_data:
		counter = counter % 3
		group[counter] = line
		
		if counter == 2:
			common_char = ''.join(set(group[0]).intersection(group[1], group[2])).replace('\n', '')
			total_prio += get_char_priority(common_char)
		
		counter += 1

	return total_prio


print("Solution part one: " + str(part_one(input_data)))
print("Solution part two: " + str(part_two(input_data)))
