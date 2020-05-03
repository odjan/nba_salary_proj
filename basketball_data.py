import requests
from urllib import request, response, error, parse
from urllib.request import urlopen
import csv
from bs4 import BeautifulSoup

source = requests.get('https://www.basketball-reference.com/leagues/NBA_2020_per_game.html').text

soup = BeautifulSoup(source, 'lxml')

article = soup.prettify()

# Finding Steven Adams
table = soup.find('table')
table_rows = table.find_all('tr')
table_headers = table.find_all('th')

# Tried to retrieve headers, but failed at this. Will try to do better next time.
""" headers =[] 
for i in table_headers:
    column_id = i.text
    headers.append(column_id) """

headers = ['Player', 'Pos', 'Age', 'Tm', 'G', 'GS', 'MP', 'FG', 'FGA', 'FG%', '3P', '3PA', '3P%', '2P', '2PA', '2P%', 'eFG%', 'FT', 'FTA', 'FT%', 'ORB', 'DRB', 'TRB', 'AST', 'STL', 'BLK', 'TOV', 'PF', 'PTS']

csv_file = open('pergame_stats.csv', 'w')
csv_writer = csv.writer(csv_file)
csv_writer.writerow(headers)


for tr in table_rows:
    td = tr.find_all('td')
    row = [i.text for i in td] #nice list comprehension to get data into lists
    csv_writer.writerow(row)

csv_file.close()



# dropping duplicates and keeping the TOT tag, i.e. Trevor Ariza [X]
# filling missing values with 0 [??]
# Dropping None types from the entire dataframe. [X]
# Find salary data and join that data with this dataframe [X]
# Cool idea would be to see which players are over/under-playing their salaries
# Calculate how many times a player has been traded [X]
# Get year player was drafted
# Calculate years of experience player has



