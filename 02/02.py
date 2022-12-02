#!/bin/python

with open("input", "r") as file:
	input_data = file.readlines()

score = 0 # overall score

# Define which player selection gives how many points
ruleset_player_selection = {"X": 1, "Y": 2, "Z": 3}

# Define which game outcome gives how many points
ruleset_game = {"lose": 0, "draw": 3, "win": 6}

for line in input_data:

	# some input validation
	if len(line.strip()) < 3:
		print("Invalid input!")
		continue

	score_current_round = 0 # score for the current input line (aka current round)
	player = line[2]
	opponent = line[0]

	# some more input validation
	if player not in ruleset_player_selection:
		print("Invalid player selection!")
		continue
	if opponent not in ["A", "B", "C"]:
		print("Invalid opponent selection!")
		continue

	score_current_round += ruleset_player_selection[player]
	
	# LET'S PLAY THE GAME
	# A / X == rock
	# B / Y == paper
	# C / Z == scissors
	if player == "X":
		if opponent == "A": score_current_round += ruleset_game["draw"]
		elif opponent == "B": score_current_round += ruleset_game["lose"]
		else: score_current_round += ruleset_game["win"]
	elif player == "Y":
		if opponent == "A": score_current_round += ruleset_game["win"]
		elif opponent == "B": score_current_round += ruleset_game["draw"]
		else: score_current_round += ruleset_game["lose"]
	else:
		if opponent == "A": score_current_round += ruleset_game["lose"]
		elif opponent == "B": score_current_round += ruleset_game["win"]
		else: score_current_round += ruleset_game["draw"]

	score += score_current_round

print("Total score: " + str(score))
