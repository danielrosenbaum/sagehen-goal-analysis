# data-cleaner.py

import csv
import random

model_data = open("model-data-adv1.csv",'w')
writer = csv.writer(model_data)

training_data = open("training-data-adv1.csv",'w')
writer_training = csv.writer(training_data)

testing_data = open("testing-data-adv1.csv",'w')
writer_testing = csv.writer(testing_data)

with open('scraped-data.csv', mode='r') as data_file:
	csv_reader = csv.DictReader(data_file)
	for data_row in csv_reader:

		# create a new row of data for the model
		model_row = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

with open('scraped-data.csv', mode='r') as data_file:
	csv_reader = csv.DictReader(data_file)
	for data_row in csv_reader:

		# create a new row of data for the model
		model_row = [0, 0, 0, 0, 0, 0, 0, 0, 0, 0]

		# NON-BINARY 
		# Values are difference of missing or making goal
		# if the goal is positive than it is completed

		# Result - positive if won, negative if lost
		model_row[0] = float(data_row['PTS (PP)']) - float(data_row['PTS (O)'])

		# GOAL 1 - shooting percentage
		model_row[1] = 100.0 * (float(data_row['FG% (PP)']) - 0.48)

		# GOAL 2 - opponent shooting percentage
		model_row[2] = 100.0 * (0.48 - float(data_row['FG% (O)']))

		# GOAL 3 - make more FT than they shoot
		model_row[3] = float(data_row['FTM (PP)']) - float(data_row['FTA (O)'])

		# GOAL 4 - out rebound the opponent
		model_row[4] = float(data_row['REB (PP)']) - float(data_row['REB (O)'])
	
		# GOAL 5 - more than 17 offensive rebounds
		model_row[5] = float(data_row['OREB (PP)']) - 17
	
		# GOAL 6 - under 12 turnovers
		model_row[6] = 12 - float(data_row['TO (PP)'])

		# GOAL 7 - force 18 or more turnovers
		model_row[7] = float(data_row['TO (O)']) - 18

		# GOAL 8 - under 30 pts in first half
		model_row[8] = 30 - float(data_row['H1 (O)'])

		# GOAL 9 - under 30 pts in second half
		model_row[9] = 30 - float(data_row['H2 (O)'])


		#  BINARY 

		# Win or Loss - Dependent Variable
		# if float(data_row['PTS (PP)']) > float(data_row['PTS (O)']):
		# 	model_row[0] = 1

		# # Independent Variables
		# # GOAL 1 - shooting percentage
		# if float(data_row['FG% (PP)']) >= 0.48:
		# 	model_row[1] = 1

		# # GOAL 2 - opponent shooting percentage
		# if float(data_row['FG% (O)']) < 0.48:
		# 	model_row[2] = 1

		# # GOAL 3 - make more FT than they shoot
		# if float(data_row['FTM (PP)']) > float(data_row['FTA (O)']):
		# 	model_row[3] = 1

		# # GOAL 4 - out rebound the opponent
		# if float(data_row['REB (PP)']) > float(data_row['REB (O)']):
		# 	model_row[4] = 1
	
		# # GOAL 5 - more than 17 offensive rebounds
		# if float(data_row['OREB (PP)']) > 17:
		# 	model_row[5] = 1
	
		# # GOAL 6 - under 12 turnovers
		# if float(data_row['TO (PP)']) < 12:
		# 	model_row[6] = 1

		# # GOAL 7 - force 18 or more turnovers
		# if float(data_row['TO (O)']) >= 18:
		# 	model_row[7] = 1

		# # GOAL 8 - under 30 pts in first half
		# if float(data_row['H1 (O)']) < 30:
		# 	model_row[8] = 1

		# # GOAL 9 - under 30 pts in second half
		# if float(data_row['H2 (O)']) < 30:
		# 	model_row[9] = 1
		
		# write that row to the model file
		writer.writerow(model_row)

		# split up testing and training data randomly 70 - 30
		if random.random() > 0.3:
			writer_training.writerow(model_row)
		else:
			writer_testing.writerow(model_row)



