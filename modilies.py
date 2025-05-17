from bs4 import BeautifulSoup
import csv

# Simulated HTML (you can replace this with actual web scraping later)
html = """
<html>
<body>
  <div class="claim">
    <p class="statement">₹15 lakh in every account</p>
    <p class="year">2014</p>
  </div>
  <div class="claim">
    <p class="statement">2 crore jobs every year</p>
    <p class="year">2014</p>
  </div>
  <div class="claim">
    <p class="statement">India became Congress-free</p>
    <p class="year">2019</p>
  </div>
</body>
</html>
"""

# Parse HTML
soup = BeautifulSoup(html, 'html.parser')
claims = soup.find_all('div', class_='claim')

# Extract data
data = []
for claim in claims:
    statement = claim.find('p', class_='statement').text.strip()
    year = claim.find('p', class_='year').text.strip()
    data.append([statement, year])

# Save to CSV
with open('modi_lies.csv', 'w', newline='', encoding='utf-8') as f:
    writer = csv.writer(f)
    writer.writerow(['Statement', 'Year'])
    writer.writerows(data)

print("Scraped data saved to modi_lies.csv")
