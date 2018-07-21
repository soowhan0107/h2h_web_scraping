from requests import get

url = "https://www.49ers.com/team/players-roster/"

response = get(url)

from bs4 import BeautifulSoup
nfl = BeautifulSoup(response.content, 'html.parser')

#print(nfl.prettify())

nfl_div = nfl.find_all('div')
#print(nfl_div)

nfl_main = nfl.find(id="main-content")
#print(nfl_main.prettify())

#find and find_all difference is that find will find the first incidence,
#find_all will find all the incidences. Output type is also different. Try yourself.

### the answer to "try yourself"

# parse into table for "Roster"
nfl_roster = nfl_main.find(summary="Roster")
#print(nfl_roster.prettify())

# parse more into <tbody> tag.
nfl_roster_body = nfl_roster.find('tbody')
#print(nfl_roster_body.prettify())

# parse more into <tr> tag.
nfl_roster_body_tr_first = nfl_roster_body.find('tr')
#print(nfl_roster_body_tr_first.prettify())


# finally, to print out the first player's college name.
# you first find all incidences of "td"s since there isn't any attribute such as id or class 
# for College table. So, we will have to manually set the index, which is 7 in this case; 7th Column = College.
# Then, we put ".text" to extract the text content, which is what we want.
first_name = nfl_roster_body_tr_first.find_all('td')[7].text
#print(first_name)


### Bonus Answer

# This is just a bit more step from the last part of the answer from try yourself question.
# We are going to iterate through the total number of players (90 in this case)
# and extract each name every loop.

# Start back from nfl_roster_body.
# Bonus 1
#for i in range(0, 90):
#	name = nfl_roster_body.find_all('tr')[i].find_all('td')[7].text
#	print(name)

# Bonus 2 - CSV college names
import csv
#for i in range(0, 90):
#    name = nfl_roster_body.find_all('tr')[i].find_all('td')[7].text
#    with open('college.csv', 'a') as csv_file:
#        writer = csv.writer(csv_file)
#        writer.writerow([name])

# Bonus 3 - Do the same for all the columns.
for i in range(0, 90):
    name = nfl_roster_body.find_all('tr')[i].find_all('td')[0].find('a').text
    number = nfl_roster_body.find_all('tr')[i].find_all('td')[1].text
    position = nfl_roster_body.find_all('tr')[i].find_all('td')[2].text
    height = nfl_roster_body.find_all('tr')[i].find_all('td')[3].text
    weight = nfl_roster_body.find_all('tr')[i].find_all('td')[4].text
    age = nfl_roster_body.find_all('tr')[i].find_all('td')[5].text
    exp = nfl_roster_body.find_all('tr')[i].find_all('td')[6].text
    college = nfl_roster_body.find_all('tr')[i].find_all('td')[7].text
    # store all to the cs
    with open('college.csv', 'a') as csv_file:
        writer = csv.writer(csv_file)
        writer.writerow([name, number, position, height, weight, age, exp, college])
