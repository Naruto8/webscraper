import bs4
import requests
from lxml import html

# Fetch the page
page = requests.get('https://www.premierleague.com/')
page.raise_for_status()
html_page = bs4.BeautifulSoup(page.text)

soup = bs4.BeautifulSoup(page.content, 'html.parser')

# Get html tag and its contents
html = list(soup.children)[2]

# Get the body of html page
body = list(html.children)[3]

# Get team's name
# team = list(soup.find_all('a', class_='matchAbridged'))[0].find_all('span', class_='teamName')[0].get_text().strip()
# matches = len(list(soup.find_all('a', class_='matchAbridged')))
# team_1 = list(soup.find_all('a', class_='matchAbridged'))[0].find_all('span', class_='score')[0].get_text().strip()
print(list(soup.find_all('a', class_='matchAbridged'))[0])
# for i in range(matches):
    # team_1 = list(soup.find_all('a', class_='matchAbridged'))[i].find_all('span', class_='score')[0].get_text().strip()
    # team_2 = list(soup.find_all('a', class_='matchAbridged'))[i].find_all('span', class_='score')[1].get_text().strip()
    # score =  list(soup.find_all('a', class_='matchAbridged'))[0].find_all('span', class_='score')[0].get_text()
    # print(team_1 + ' ' + score + ' ' + team_2)

# Get score
# score = list(soup.find_all('a', class_='matchAbridged'))[0].find_all('span', class_='score')[0].get_text()
