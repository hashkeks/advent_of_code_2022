#!/bin/python
import string

with open("input", "r") as file:
	input_data = file.readlines()

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
	if not common_char.isalpha():	# checking for other stupid chars like \n
		continue

	total_prio += (ord(common_char) - 96) if common_char.islower() else (ord(common_char) - 38)

print(total_prio)
