#!/bin/python

with open("input", "r") as file:
	input_data = file.readlines()


def get_priority(char):
	return (ord(char) - 96) if char.islower() else (ord(char) - 38)


def part_one(input_data):
	total_prio = 0

	for line in input_data:
		middle = int((len(line)/2))	# cast to integer to use it as index
		left = line[:middle]
		right = line[middle:]
	
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
	
		total_prio += get_priority(common_char)
	
	return total_prio


#def part_two(input_data):


print("Solution part one: " + str(part_one(input_data)))
