#!/usr/bin/python3.4

import random

colorsEnabled = True

class color:
    OUTCOME = '\033[95m' if colorsEnabled else ''
    GREEN = '\033[92m' if colorsEnabled else ''
    DRAW = '\033[93m' if colorsEnabled else ''
    RED = '\033[91m' if colorsEnabled else ''
    END = '\033[0m' if colorsEnabled else ''

outcomes = (
	"Scissors cut paper",
	"Paper covers rock",
	"Rock crushes lizard",
	"Lizard poisons Spock",
	"Spock smashes scissors",
	"Scissors decapitate lizard",
	"Lizard eats paper",
	"Paper disproves Spock",
	"Spock vaporizes rock",
	"Rock crushes scissors"
)

moves = (
	"scissors",
	"paper",
	"rock",
	"lizard",
	"spock"
)

gamesPlayed = 0
gamesLost = 0
gamesWon = 0
gamesDraw = 0

if __name__ == "__main__":
	while True:
		while True:
			ply = input("\033[92mPlayer\033[0m Picks: ")
			ply = ply.lower()

			if ply in moves:
				break

			print("Unrecognized move! Available moves: ")
			for move in moves:
				print(move)
			print()

		com = random.choice(moves)

		for outcome in outcomes:
			if outcome.lower().find(ply) == -1 or outcome.lower().find(com) == -1:
				continue

			if outcome.lower().find(ply) == 0 and outcome.lower().find(com) != 0:
				winner = color.GREEN + "Player"
				result = outcome
				draw = False
				gamesWon += 1
				break
			elif outcome.lower().find(ply) != 0 and outcome.lower().find(com) == 0:
				winner = color.RED + "Computer"
				result = outcome
				draw = False
				gamesLost += 1
				break
			else:
				draw = True

		gamesPlayed += 1

		print(color.RED + "Computer " + color.END + "Picks: %s" % com)
		print("")

		if draw:
			print(color.OUTCOME + "You did the same move" + ". " + color.DRAW + "Draw" + color.END)
			gamesDraw += 1
		else:
			print( color.OUTCOME + outcome + ". " + winner + " Wins!" + color.END)

		stats = """
			STATS:
			Played: {}
			{}Won:{} {} [{}%]
			{}Lost:{} {} [{}%]
			{}Draw:{} {} [{}%]
			""".format(gamesPlayed, color.GREEN, color.END, gamesWon, int(gamesWon/gamesPlayed*100), color.RED, color.END, gamesLost, int(gamesLost/gamesPlayed*100), color.DRAW, color.END, gamesDraw, int(gamesDraw/gamesPlayed*100) )
		print( stats )