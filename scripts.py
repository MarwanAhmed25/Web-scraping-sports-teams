import requests
from bs4 import BeautifulSoup

# URL of the webpage to scrape
url = "https://www.espn.com/nba/standings"

# Send a GET request to the URL and store the response
response = requests.get(url)

# Parse the HTML content of the response using BeautifulSoup
soup = BeautifulSoup(response.content, "html.parser")

# Find the table containing the standings data
standings_table = soup.find("table", class_="standings has-team-logos")

# Extract the column headers from the table
headers = [th.text for th in standings_table.find_all("th")]

# Extract the rows of data from the table
rows = []
for tr in standings_table.find_all("tr"):
    row = [td.text for td in tr.find_all("td")]
    if row:
        rows.append(row)

# Print the column headers and data rows
print(headers)
for row in rows:
    print(row)
