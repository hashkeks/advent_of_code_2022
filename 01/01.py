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

def get_max(lst):
	current = lst[0]

	for entry in lst:
		if entry > current:
			current = entry
	return current


		
print(get_max(feed(input_data)))

