# model.py

# Based on the binary model data, create a model and make some predictions

import csv
import matplotlib.pyplot as plt
from sklearn.linear_model import LinearRegression
from sklearn import preprocessing

# read in training data
with open('data/training-data-adv1.csv', mode='r') as training_data:
	csv_reader = csv.reader(training_data)
	X = []
	Y = []

	for row in csv_reader:
		X.append([float(elt) for elt in row[1:]]) 
		Y.append(float(row[0]))

# read in testing data
with open('data/testing-data-adv1.csv', mode='r') as testing_data:
	csv_reader = csv.reader(testing_data)
	X_test = []
	Y_test = []

	for row in csv_reader:
		X_test.append([float(elt) for elt in row[1:]])
		Y_test.append(float(row[0]))

# Regression time
# create the model
model = LinearRegression().fit(preprocessing.scale(X), Y)
print("Score: ", (model.score(X, Y))) # R^2 value
print("Coefficients: ", model.coef_)

# make predictions
Y_hat = model.predict(X_test)

plt.plot(X_test, Y_test)
# get results from our predictions
total = wins = predicted_wins = 0
for result, prediction in zip(Y_test, Y_hat):
	total += 1
	
	if result > 0:
		wins += 1
	
	if prediction >= 0:
		predicted_wins += 1

# print results
print ("# Wins: ", wins)
print ("# Pred. Wins: ", predicted_wins)
print ("# Losses: ", total - wins)
print ("# Pred. Losses: ",total - predicted_wins)

# plot the results
goal_one   = [row[0] for row in X_test]
goal_two   = [row[1] for row in X_test]
goal_three = [row[2] for row in X_test]
goal_four  = [row[3] for row in X_test]
goal_five  = [row[4] for row in X_test]
goal_six   = [row[5] for row in X_test]
goal_seven = [row[6] for row in X_test]
goal_eight = [row[7] for row in X_test]
goal_nine  = [row[8] for row in X_test]

plt.ylabel("Score Difference")
plt.plot(goal_one, Y_hat)
plt.scatter(goal_one, Y_test,  color='black')
plt.xlabel("Shooting Percentage - 0.48")
plt.show()

plt.scatter(goal_two, Y_test,  color='blue')
plt.xlabel("0.48 - Opponent Percentage")
plt.show()

plt.scatter(goal_three, Y_test,  color='red')
plt.xlabel("Free Throws (Makes - Opponent Attempts)")
plt.show()

plt.scatter(goal_four, Y_test,  color='orange')
plt.xlabel("Rebound Difference")
plt.show()

plt.scatter(goal_five, Y_test,  color='purple')
plt.xlabel("Offensive Rebounds - 17")
plt.show()

plt.scatter(goal_six, Y_test,  color='pink')
plt.xlabel("12 - Turnovers")
plt.show()

plt.scatter(goal_seven, Y_test,  color='green')
plt.xlabel("Opponent Turnovers - 18")
plt.show()

plt.scatter(goal_eight, Y_test,  color='brown')
plt.xlabel("30 - Opponent First Half")
plt.show()

plt.scatter(goal_nine, Y_test,  color='yellow')
plt.xlabel("30 - Opponent Second Half")
plt.show()
