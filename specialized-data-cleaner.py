# specialized-data-cleaner.py

import csv
import random

model_data_adv = open("data/spec-model-data-adv.csv",'w')
model_data_bin = open("data/spec-model-data-bin.csv",'w')
writer_adv = csv.writer(model_data_adv)
writer_bin = csv.writer(model_data_bin)

training_data_adv = open("data/spec-training-data-adv.csv",'w')
training_data_bin = open("data/spec-training-data-bin.csv",'w')
writer_training_adv = csv.writer(training_data_adv)
writer_training_bin = csv.writer(training_data_bin)

testing_data_adv = open("data/spec-testing-data-adv.csv",'w')
testing_data_bin = open("data/spec-testing-data-bin.csv",'w')
writer_testing_adv = csv.writer(testing_data_adv)
writer_testing_bin = csv.writer(testing_data_bin)

with open('data/scraped-data.csv', mode='r') as data_file:
	csv_reader = csv.DictReader(data_file)
	for data_row in csv_reader:

		# NON-BINARY - Advanced
		# Values are difference of missing or making goal
		# if the goal is positive than it is completed

		# create a new empty row of data for the model
		model_row = [0, 0, 0, 0, 0, 0, 0, 0]

		# Result - positive if won, negative if lost
		model_row[0] = float(data_row['PTS (PP)']) - float(data_row['PTS (O)'])

		# GOAL 1 - shooting percentage
		model_row[1] = 100.0 * (float(data_row['FG% (PP)']) - 0.48)

		# GOAL 2 - opponent shooting percentage
		model_row[2] = 100.0 * (0.40 - float(data_row['FG% (O)']))

		# GOAL 3 - make more FT than they shoot
		model_row[3] = float(data_row['FTM (PP)']) - float(data_row['FTA (O)'])

		# GOAL 4 - out rebound the opponent
		model_row[4] = float(data_row['REB (PP)']) - float(data_row['REB (O)'])

		# # GOAL 5 - more than 17 offensive rebounds
		# model_row[5] = float(data_row['OREB (PP)']) - 17

		# GOAL 6 - under 12 turnovers
		model_row[5] = 12 - float(data_row['TO (PP)'])

		# # GOAL 7 - force 18 or more turnovers
		# model_row[7] = float(data_row['TO (O)']) - 18

		# GOAL 8 - under 30 pts in first half
		model_row[6] = 30 - float(data_row['H1 (O)'])

		# GOAL 9 - under 30 pts in second half
		model_row[7] = 30 - float(data_row['H2 (O)'])


		# BINARY
		# Either the goal was achieved or not

		# create a new row of data for the model
		model_row_bin = [0, 0, 0, 0, 0, 0]

		# Win or Loss - Dependent Variable
		if float(data_row['PTS (PP)']) > float(data_row['PTS (O)']):
			model_row_bin[0] = 1

		# Independent Variables
		# GOAL 1 - shooting percentage
		if float(data_row['FG% (PP)']) >= 0.48:
			model_row_bin[1] = 1

		# GOAL 2 - opponent shooting percentage
		if float(data_row['FG% (O)']) < 0.40:
			model_row_bin[2] = 1

		# GOAL 4 - out rebound the opponent
		if float(data_row['REB (PP)']) > float(data_row['REB (O)']):
			model_row_bin[3] = 1

		# GOAL 6 - under 12 turnovers
		if float(data_row['TO (PP)']) < 12:
			model_row_bin[4] = 1

		# GOAL 7 - force 18 or more turnovers
		if float(data_row['TO (O)']) >= 18:
			model_row_bin[5] = 1


		# Writing the cleaned data

		# write that row to the model file
		writer_adv.writerow(model_row)
		writer_bin.writerow(model_row_bin)

		# split up testing and training data randomly 70 - 30
		if random.random() > 0.3:
			writer_training_adv.writerow(model_row)
			writer_training_bin.writerow(model_row_bin)
		else:
			writer_testing_adv.writerow(model_row)
			writer_testing_bin.writerow(model_row_bin)
