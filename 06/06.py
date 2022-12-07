#!/bin/python

with open("input", "r") as file:
	input_data = file.readline()


def find_markers(input_data, num_unique_chars):

	for i in range(len(input_data)):
		# Use the characteristic of a set, that it can't contain two of the same
		# objects. 
		# Iterating through the string, at each char a set is created with the char
		# + the next num_unique_chars number of chars. If every char is unique, we 
		# have a set with the length of num_unique_chars.
		marker = set(input_data[i:i+num_unique_chars])
		if len(marker) == num_unique_chars:
			return i + num_unique_chars	
	return 0


print("Solution part one: " + str(find_markers(input_data, 4)))
print("Solution part two: " + str(find_markers(input_data, 14)))
