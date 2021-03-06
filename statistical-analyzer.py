# statistical-analyzer.py

# Question: Which goal leads to the most wins

# Goals
# 1. Shoot better than 48% from the field
# 2. Hold the opponent under 40% from the field
# 3. Make more free throws than the opponent shoots
# 4. Outrebound the opponent
# 5. 17 or more offensive rebounds
# 6. Under 12 turnovers
# 7. Force 18 or more turnovers
# 8. Hold opponent under 30 pts (First Half)
# 9. Hold opponent under 30 pts (Second Half)

# Data Columns
# FGM (PP), FGA (PP), 3PM (PP), 3PA (PP), FTM (PP), FTA (PP), OREB (PP), DREB (PP), REB (PP), AST (PP), STL (PP), BLK (PP), TO (PP), PF (PP), PTS (PP), FG% (PP), 3P% (PP), FT% (PP), H1 (PP), H2 (PP)
# FGM (O), FGA (O), 3PM (O), 3PA (O), FTM (O), FTA (O), OREB (O), DREB (O), REB (O), AST (O), STL (O), BLK (O), TO (O), PF (O), PTS (O), FG% (O), 3P% (O), FT% (O), H1 (O), H2 (O)

import csv

games = wins = 0
g_one = g_two = g_three = g_four = g_five = g_six = g_seven = g_eight = g_nine = 0
gc_one = gc_two = gc_three = gc_four = gc_five = gc_six = gc_seven = gc_eight = gc_nine = 0


with open('data/scraped-data.csv', mode='r') as data_file:
	csv_reader = csv.DictReader(data_file)
	for row in csv_reader:
		games += 1
		wins += 1 if float(row['PTS (PP)']) > float(row['PTS (O)']) else  0

		# How many wins did you get, if you completed the goal?

		# GOAL 1 - shooting percentage
		if float(row['FG% (PP)']) >= 0.48:
			g_one += 1
			game_goal += 1
			if float(row['PTS (PP)']) > float(row['PTS (O)']):
				gc_one += 1

		# GOAL 2 - opponent shooting percentage
		if float(row['FG% (O)']) < 0.40:
			g_two += 1
			game_goal += 1
			if float(row['PTS (PP)']) > float(row['PTS (O)']):
				gc_two += 1

		# GOAL 3 - make more FT than they shoot
		if float(row['FTM (PP)']) > float(row['FTA (O)']):
			g_three += 1
			game_goal += 1
			if float(row['PTS (PP)']) > float(row['PTS (O)']):
				gc_three += 1

		# GOAL 4 - out rebound the opponent
		if float(row['REB (PP)']) > float(row['REB (O)']):
			g_four += 1
			game_goal += 1
			if float(row['PTS (PP)']) > float(row['PTS (O)']):
				gc_four += 1

		# GOAL 5 - more than 17 offensive rebounds
		if float(row['OREB (PP)']) > 17:
			g_five += 1
			game_goal += 1
			if float(row['PTS (PP)']) > float(row['PTS (O)']):
				gc_five += 1

		# GOAL 6 - under 12 turnovers
		if float(row['TO (PP)']) < 12:
			g_six += 1
			game_goal += 1
			if float(row['PTS (PP)']) > float(row['PTS (O)']):
				gc_six += 1

		# GOAL 7 - force 18 or more turnovers
		if float(row['TO (O)']) >= 15:
			g_seven += 1
			game_goal += 1
			if float(row['PTS (PP)']) > float(row['PTS (O)']):
				gc_seven += 1

		# GOAL 8 - under 30 pts in first half
		if float(row['H1 (O)']) < 20:
			g_eight += 1
			game_goal += 1
			if float(row['PTS (PP)']) > float(row['PTS (O)']):
				gc_eight += 1

		# GOAL 9 - under 30 pts in second half
		if float(row['H2 (O)']) < 30:
			g_nine += 1
			game_goal += 1
			if float(row['PTS (PP)']) > float(row['PTS (O)']):
				gc_nine += 1

# Print the results to the console
print ("Games:\t\t{}".format(games))
print ("Wins:\t\t{}".format(wins))
print ("Goal\t\t\t#Won\t#Total\t#Won/#Total")
print ("Shoot 48%:\t\t{}\t{}\t{}".format(gc_one, g_one, gc_one/g_one))
print ("Hold Under 40%:\t\t{}\t{}\t{}".format(gc_two, g_two, gc_two/g_two))
print ("Free Throws:\t\t{}\t{}\t{}".format(gc_three, g_three, gc_three/g_three))
print ("Out Rebound:\t\t{}\t{}\t{}".format(gc_four, g_four, gc_four/g_four))
print ("Offensive Rebounds:\t{}\t{}\t{}".format(gc_five, g_five, gc_five/g_five))
print ("Under Turnovers:\t{}\t{}\t{}".format(gc_six, g_six, gc_six/g_six))
print ("Force Turnovers:\t{}\t{}\t{}".format(gc_seven, g_seven, gc_seven/g_seven))
print ("First Half:\t\t{}\t{}\t{}".format(gc_eight, g_eight, gc_eight/g_eight))
print ("Second Half:\t\t{}\t{}\t{}".format(gc_nine, g_nine, gc_nine/g_nine))
