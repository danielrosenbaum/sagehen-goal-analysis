# model.py

# Create a model and make some predictions

import csv
import matplotlib.pyplot as plt
import numpy as np
from sklearn.linear_model import LinearRegression
from sklearn.neural_network import MLPClassifier
from sklearn.neural_network import MLPRegressor
from sklearn import preprocessing


# read in training data
with open('data/adj-training-data-adv.csv', mode='r') as training_data:
	csv_reader = csv.reader(training_data)
	X = []
	Y = []

	for row in csv_reader:
		X.append([float(elt) for elt in row[1:]])
		Y.append(float(row[0]))

# read in testing data
with open('data/adj-testing-data-adv.csv', mode='r') as testing_data:
	csv_reader = csv.reader(testing_data)
	X_test = []
	Y_test = []

	for row in csv_reader:
		X_test.append([float(elt) for elt in row[1:]])
		Y_test.append(float(row[0]))

### SCALING Data

X = preprocessing.scale(X)
X_test = preprocessing.scale(X_test)


### MODELS

# Linear regression

model = LinearRegression().fit(X, Y)
Y_hat = model.predict(X_test)

# get results from our predictions
total = predicted_losses = predicted_wins = correct = wins = 0
for result, prediction in zip(Y_test, Y_hat):
	total += 1
	wins += 1 if result > 0 else 0

	if result > 0 and prediction > 0:
		predicted_wins += 1
		correct += 1
	elif result < 0 and prediction < 0:
		predicted_losses += 1
		correct += 1

print("LinearRegression")
print ("# Wins: ", wins)
print ("# Pred. Wins: ", predicted_wins)
print ("# Losses: ", total - wins)
print ("# Pred. Losses: ",predicted_losses)
print ("# Correct: ", correct)
print ("Total: ", total)

print("Score: ", model.score(X, Y)) # R^2 value
print("Coefficients: ", model.coef_)


# Multi Layer Perceptron Regressor

regressor = MLPRegressor(activation='relu', max_iter=1000).fit(X, Y)
reg_Y_hat = regressor.predict(X_test)

# get results from our predictions
reg_total = reg_predicted_losses = reg_predicted_wins = reg_correct = reg_wins = 0
for reg_result, reg_prediction in zip(Y_test, reg_Y_hat):
	reg_total += 1
	reg_wins += 1 if reg_result > 0 else 0

	if reg_result > 0 and reg_prediction > 0:
		reg_predicted_wins += 1
		reg_correct += 1
	elif reg_result < 0 and reg_prediction < 0:
		reg_predicted_losses += 1
		reg_correct += 1

print("MLPRegressor")
print ("# Wins: ", reg_wins)
print ("# Pred. Wins: ", reg_predicted_wins)
print ("# Losses: ", reg_total - reg_wins)
print ("# Pred. Losses: ", reg_predicted_losses)
print ("# Correct: ", reg_correct)
print ("Total: ", reg_total)
# print(regressor.coefs_)


### GRAPHS

total_X = X + X_test
total_Y = Y + Y_test

# plot the results
goal_one   = [[row[0]] for row in total_X]
goal_two   = [[row[1]] for row in total_X]
goal_three = [[row[2]] for row in total_X]
goal_four  = [[row[3]] for row in total_X]
goal_five  = [[row[4]] for row in total_X]
goal_six   = [[row[5]] for row in total_X]
goal_seven = [[row[6]] for row in total_X]
goal_eight = [[row[7]] for row in total_X]
goal_nine  = [[row[8]] for row in total_X]

goals = [goal_one, goal_two, goal_three, goal_four, goal_five, goal_six, goal_seven, goal_eight, goal_nine]

# Create the figure and the plot
fig, axs = plt.subplots(3, 3, sharey=True)
plt.subplots_adjust(hspace=0.5)
fig.text(0.06, 0.5, 'Score Difference', ha='center', va='center', rotation='vertical')
for i in range(0,3):
	for j in range(0,3):
		# show grid lines and axis
		axs[i,j].grid(axis="both")
		axs[i,j].axhline(0)
		axs[i,j].axvline(0)

		# linear regression for each goal scatter
		goal_X = goals[i*3 + j]
		model = LinearRegression().fit(goal_X, total_Y)
		pred_Y = model.predict(goal_X)
		print(model.score(goal_X, total_Y))
		axs[i,j].plot(goal_X, pred_Y, color="black")
		axs[i,j].text(0.05, 0.95, round(model.score(goal_X, total_Y), 3), ha='left', va='top', transform=axs[i,j].transAxes)
# Goal One
axs[0,0].scatter(goal_one, total_Y,  color='grey')
axs[0,0].set_xlabel("Shooting Percentage - 0.48")

# Goal Two
axs[0,1].scatter(goal_two, total_Y,  color='blue')
axs[0,1].set_xlabel("0.40 - Opponent Percentage")

# Goal Three
axs[0,2].scatter(goal_three, total_Y,  color='red')
axs[0,2].set_xlabel("Free Throws (Makes - Opponent Attempts)")

# Goal Four
axs[1,0].scatter(goal_four, total_Y,  color='orange')
axs[1,0].set_xlabel("Rebound Difference")

# Goal Five
axs[1,1].scatter(goal_five, total_Y,  color='purple')
axs[1,1].set_xlabel("Offensive Rebounds - 17")

# Goal Six
axs[1,2].scatter(goal_six, total_Y,  color='pink')
axs[1,2].set_xlabel("12 - Turnovers")

# Goal Seven
axs[2,0].scatter(goal_seven, total_Y,  color='green')
axs[2,0].set_xlabel("Opponent Turnovers - 18")

# Goal Eight
axs[2,1].scatter(goal_eight, total_Y,  color='brown')
axs[2,1].set_xlabel("30 - Opponent First Half")

# Goal Nine
axs[2,2].scatter(goal_nine, total_Y,  color='yellow')
axs[2,2].set_xlabel("30 - Opponent Second Half")

plt.show()


# FG% and WINS PER SEASON

fg = [[48.9], [49.8], [46], [45.2], [40.3], [41.3], [43.3], [42.3], [44], [36.8], [41.8], [44.4], [40.4], [45]]
ws = [24, 26, 15, 14, 12, 10, 18, 14, 16, 9, 14, 15, 15, 16]

model = LinearRegression().fit(fg, ws)
pred_Y = model.predict(fg)
print(model.score(fg, ws))

plt.scatter(fg, ws)
plt.plot(fg, pred_Y, color="blue")
plt.grid(axis="both")
plt.xlabel("Average Field Goal Percentage")
plt.ylabel("# of Wins")
plt.title("Field Goal Percentage and Wins")
plt.yticks([8, 11, 14, 17, 20, 23, 26])

plt.show()
