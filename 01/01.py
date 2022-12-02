#!/bin/python

with open("input", "r") as file:
	input_data = file.readlines()

def feed(input_data):
	cal_list = []
	counter = 0
	for line in input_data:
		if line != '\n':
			if counter == len(cal_list):
				cal_list.append(int(line.strip()))
			else:
				cal_list[counter] += int(line.strip())
		else:
			counter += 1
	return cal_list	

cal_list = feed(input_data)

# for part one
def get_max_cal(lst):
	current = lst[0]

	for entry in lst:
		if entry > current:
			current = entry
	return current

# for part two
def get_top_three_total_cal(lst):
	first = lst[0]
	second = lst[1]
	third = lst[2]

	for entry in lst:
		if entry > first:
			third = second
			second = first
			first = entry
		elif entry > second:
			third = second
			second = entry
		elif entry > third:
			third = entry

	print(first)
	print(second)
	print(third)
	return (first + second + third)
	
print("Solution for part one: " + str(get_max_cal(cal_list)))
print("\nSolution for part two: " + str(get_top_three_total_cal(cal_list)))


