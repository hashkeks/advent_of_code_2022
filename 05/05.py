#!/bin/python

with open('input', 'r') as file:
	input_data = file.readlines()

stacks = [
	[],	#1
	[],	#2
	[], #3
	[], #4
	[], #5
	[], #6
	[], #7
	[], #8
	[]	#9
]

def load_stacks(input_data, n=4):

	 # 'n' is the  number of characters between stacks
	for line in input_data:
		
		if line[1].isnumeric():
			break
		
		for i in range(0, len(line), n):
			# 'crate' will be empty when there is no crate and the current
			# position is skipped
			crate = line[i:i+n].replace('\n', '').strip()

			if crate == '':
				continue
			else:
				# Get the current stack number, will be 0, 1, 2, etc. dependent
				# on which position i+n currently is at
				index = int(((i+n)/4)-1)
				stacks[index].insert(0, crate)

# Takes an argument if we use part one or part two mechanic
def move_around(input_data, part):

	for line in input_data:
		# Skip the stack setup
		if not line[0] == 'm':
			continue

		line = line.replace('\n', '').split(' ')
		print(line)

		# line[1] = number of crates to move
		# line[5] = where to move the crates to
		# line[3] = from where to take the crates

		if part == 'one':
			for i in range(int(line[1])):
				stacks[int(line[5])-1].append(stacks[int(line[3])-1].pop())
		elif part == 'two':
			fromStack = stacks[int(line[3])-1]
			toStack = stacks[int(line[5])-1]
			insertPoint = len(toStack)
			for i in range(int(line[1])):
				toStack.insert(insertPoint, fromStack.pop())
		else:
			print("What game are you playin?!")

load_stacks(input_data, 4)
# Decide which part to solve: 'one' or 'two'
move_around(input_data, 'two')

for i in range(0, 9):
	print(stacks[i].pop(), end='')
