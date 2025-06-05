import csv
import json

new_headers = ["title", "price"]

data = []

with open("activity.csv", mode="r", encoding="utf-8") as tsv_file:
    reader = csv.DictReader(tsv_file, delimiter='\t', fieldnames=new_headers)
    next(reader) #跳過header，因爲前面有放header
    for row in reader:
        # 轉換資料形態
        try:
            row['price'] = int(row['price'])
        except ValueError:
            row['price'] = None
        data.append(row)

data_json = json.dumps(data, ensure_ascii=False, indent=2)
print(data_json)
