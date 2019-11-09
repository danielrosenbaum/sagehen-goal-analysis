# sagehens-scraper.py

# Get box score data from Sagehens.com basketball team seasons

from selenium import webdriver
from selenium.webdriver import Safari
import csv

# create our output csv file 
output_data = open("data.csv",'w')
writer = csv.writer(output_data)

years = ['2018-19', '2017-18', '2016-17', '2015-16', '2014-15', '2013-14', '2012-13', '2011-12']
url = 'https://www.sagehens.com/sports/mbkb/{}/teams/pomonapitzer?view=gamelog'

# create the driver
driver = webdriver.Safari()

# get all the years data
for year in years:
	
	# go to specific year url
	driver.get(url.format(year))

	# get the whole table
	table = driver.find_element_by_xpath('//*[@id="mainbody"]/div[1]/div[2]/div[2]/div[3]/div/div/div/div/table/tbody')

	# get all the links to box scores in the table
	box_score_links = table.find_elements_by_tag_name('a')

	links = []
	for elt in box_score_links:
		links.append(elt.get_attribute('href'))

	# go to each box score to get the data
	for link in links:
		driver.get(link)

		# away team
		away_totals = driver.find_element_by_xpath('//*[@id="mainbody"]/article/div[2]/div[2]/section[1]/div[1]/div[2]/div/div/div/table/tbody[3]')
		away_values = away_totals.find_elements_by_tag_name('td')

		# home team
		home_totals = driver.find_element_by_xpath('//*[@id="mainbody"]/article/div[2]/div[2]/section[1]/div[1]/div[3]/div/div/div/table/tbody[3]')
		home_values = home_totals.find_elements_by_tag_name('td')

		# add in half time scores
		home_first_half = driver.find_element_by_xpath('//*[@id="mainbody"]/article/div[1]/div/div[3]/table/tbody/tr[3]/td[1]')
		home_second_half = driver.find_element_by_xpath('//*[@id="mainbody"]/article/div[1]/div/div[3]/table/tbody/tr[3]/td[2]')
		away_first_half = driver.find_element_by_xpath('//*[@id="mainbody"]/article/div[1]/div/div[3]/table/tbody/tr[2]/td[1]')
		away_second_half = driver.find_element_by_xpath('//*[@id="mainbody"]/article/div[1]/div/div[3]/table/tbody/tr[2]/td[2]')

		# see if PP was home or away team
		away_team_name = driver.find_element_by_xpath('//*[@id="mainbody"]/article/div[2]/div[2]/section[1]/div[1]/div[2]/div/div/div/table/caption/h2/span')
		
		# now create one row of data such that it is | PP | Opponent |
		row = []
		
		if away_team_name.text == "Pomona-Pitzer":
			for val in away_values:
				row.append(val.text.strip().split('-'))
			row.append([away_first_half.text])
			row.append([away_second_half.text])

			for val in home_values:
				row.append(val.text.strip().split('-'))
			row.append([home_first_half.text])
			row.append([home_second_half.text])

			row.append(["A"]) # mark PP was away team

		else: 
			for val in home_values:
				row.append(val.text.strip().split('-'))
			row.append([home_first_half.text])
			row.append([home_second_half.text])

			for val in away_values:
				row.append(val.text.strip().split('-'))
			row.append([away_first_half.text])
			row.append([away_second_half.text])

			row.append("H") # mark PP was home team

		# format the row evenly
		row = [[elt for a in row for elt in a]]
		print(row)
		
		# write that row to a csv file
		writer.writerows(row)

# program complete, close the driver
driver.quit()