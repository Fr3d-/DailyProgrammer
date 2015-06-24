#!/usr/bin/python3.4

import random
import operator

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

counters = (
	("spock", "rock"),
	("scissors", "lizard"),
	("paper", "spock"),
	("rock", "scissors"),
	("lizard", "paper")
)

choices = [0, 0, 0, 0, 0]

gamesPlayed = 0
gamesLost = 0
gamesWon = 0
gamesDraw = 0

def calculateMove():
	bestCounters = []

	for k, choice in enumerate(choices):
		if choice == max(choices):
			bestCounters.extend(counters[k])

	return random.choice(bestCounters)


if __name__ == "__main__":
	while True:
		while True:
			num = input("\033[92mPlayer\033[0m Picks: ")
			
			try:
				if num == "q":
					raise SystemExit

				num = int(num)
				if num <= 4 and num >= 0:
					ply = moves[num]
					break
			except ValueError:
				pass

			print("Unrecognized move! Available moves: ")
			i = 0
			for move in moves:
				print( str(i) + " - " + move)
				i += 1
			print("\nq - Quit\n")

		com = calculateMove()

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

		choices[num] += 1