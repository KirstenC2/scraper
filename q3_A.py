import json
import requests
import csv

new_headers = ["title", "price"]

data = []

with open("activity.csv", mode="r", encoding="utf-8") as tsv_file:
    reader = csv.DictReader(tsv_file, delimiter='\t', fieldnames=new_headers)
    next(reader) 
    for row in reader:
        try:
            row['price'] = int(row['price'])
        except ValueError:
            row['price'] = None
        data.append(row)

data_json = json.dumps(data, ensure_ascii=False, indent=2)
print(data_json)

url = "https://api.schedule.asiayo.com/"

headers = {
    "channel": "CP",
    "user": "rpa",
    "contentType": "application/JSON"
}


payload = json.loads(data_json)

response = requests.post(url, headers=headers, json=payload)

