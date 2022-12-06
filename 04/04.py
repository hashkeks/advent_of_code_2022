#!/bin/python

with open("input", "r") as file:
	input_data = file.readlines()

complete_overlaps = 0
partly_overlaps = 0

for line in input_data:
	
	line = line.replace(',', '-')
	aBegin, aEnd, zBegin, zEnd = map(int, line.split('-'))

	# part one
	if (aBegin <= zBegin and zEnd <= aEnd) or (zBegin <= aBegin and aEnd <= zEnd):
		complete_overlaps += 1	

	# part  two
	if aBegin <= zBegin <= aEnd or aBegin <= zEnd <= aEnd or zBegin <= aBegin <= zEnd or zBegin <= aEnd <= zEnd:
		partly_overlaps += 1

print("Solution part one: " + str(complete_overlaps))
print("Solution part two: " + str(partly_overlaps))
