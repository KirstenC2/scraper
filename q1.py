import requests
from bs4 import BeautifulSoup
import csv
import re 

# 1. Fetch the HTML from a webpage
url = "https://asiayo.com/zh-tw/package/sport-activities/" 
response = requests.get(url)
html = response.text

# 2. Parse with BeautifulSoup
soup = BeautifulSoup(html, "html.parser")

# 3. 
wrappers = soup.find_all("div", {"data-sentry-element": "ContentWrapper"})

# 4. Extract data
data = []
for block in wrappers:
    title_tag = block.find("h2")
    price_tag = block.find("div", class_="sc-2bb56610-10 kfdgWe")

    if title_tag and price_tag:
        raw_title = title_tag.get_text(strip=True)
        # Remove date in format YYYY/MM/DD
        title = re.sub(r'【.*?】|\s*\d{4}/\d{2}/\d{2}', '', raw_title)

        raw_price = price_tag.get_text(strip=True)
        match = re.search(r'\d[\d,]*', raw_price)
        price = match.group().replace(',', '') if match else ''

        data.append({"賽事名稱": title, "每人最低價": price})


# 5. Save to CSV
filename = "activity.csv"
with open(filename, mode="w", newline="", encoding="utf-8") as file:
    writer = csv.DictWriter(file, fieldnames=["賽事名稱", "每人最低價"], delimiter='\t')
    writer.writeheader()
    writer.writerows(data)

print(f"共 {len(data)} 資料以寫入 {filename}")
