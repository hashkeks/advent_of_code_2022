#!/bin/python

with open("input", "r") as file:
	input_data = file.readlines()

# Define which player selection gives how many points
ruleset_player_selection = {"X": 1, "Y": 2, "Z": 3}

# Define which game outcome gives how many points
ruleset_game = {"lose": 0, "draw": 3, "win": 6}


#for part one
def fair_match(player, opponent):
	# LET'S PLAY THE GAME
	# A / X == rock
	# B / Y == paper
	# C / Z == scissors
	if player == "X":
		if opponent == "A": return ruleset_game["draw"]
		elif opponent == "B": return ruleset_game["lose"]
		else: return ruleset_game["win"]
	elif player == "Y":
		if opponent == "A": return ruleset_game["win"]
		elif opponent == "B": return ruleset_game["draw"]
		else: return ruleset_game["lose"]
	else: # player == "Z"
		if opponent == "A": return ruleset_game["lose"]
		elif opponent == "B": return ruleset_game["win"]
		else: return ruleset_game["draw"]


# for part two
# since XYZ is not the player's selection anymore but indicates how to play, we
# need a mapping to make it still compatible with ruleset_player_selection in
# case of a draw
pairs = {"A": "X", "B": "Y", "C": "Z"}

def super_fair_match(opponent, strategy):
	# LET'S PLAY THE GAME AGAIN >:D
	# A == rock			X == lose
	# B == paper		Y == draw
	# C == scissors		Z == win

	# ...and no, I don't wanna implement a ring buffer with easier access for
	# only three values...
	# What the weird calculation for "player" does: Just going one forward or
	# backward from ASCII number 65 (A) to 67 (C). Modulo 3 because we don't
	# want to go over 67 or below 65.
	if strategy == "X":
		player = chr(65 + ((ord(opponent) - 65 - 1) % 3))
		points = ruleset_game["lose"] + ruleset_player_selection[pairs[player]]
	elif strategy == "Y":
		points = ruleset_game["draw"] + ruleset_player_selection[pairs[opponent]]
	else: # strategy == "Z"
		player = chr(65 + ((ord(opponent) - 65 + 1) % 3))
		points = ruleset_game["win"] + ruleset_player_selection[pairs[player]]

	return points


score = 0		# part one
fair_score = 0	# part two

for line in input_data:

	# some input validation
	if len(line.strip()) < 3:
		print("Invalid input!")
		continue

	player = line[2]
	opponent = line[0]

	# some more input validation
	if player not in ruleset_player_selection:
		print("Invalid player selection!")
		continue
	if opponent not in ["A", "B", "C"]:
		print("Invalid opponent selection!")
		continue

	### PART ONE ###
	################
	# score calculation
	score_current_round = (ruleset_player_selection[player] + fair_match(player, opponent))
	score += score_current_round

	### PART TWO ###
	###############
	fair_score += super_fair_match(opponent, player) # be aware of the function variable swap!
	
print("Solution part one: " + str(score))
print("Solution part two: " + str(fair_score))
