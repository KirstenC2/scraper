import csv
import json

new_headers = ["title", "price"]

data = []

with open("activity.csv", mode="r", encoding="utf-8") as tsv_file:
    reader = csv.DictReader(tsv_file, delimiter='\t', fieldnames=new_headers)
    next(reader)  # 跳過原本的標題列
    for row in reader:
        # 轉換 price 為整數，如果不能轉就設成 None 或 0
        try:
            row['price'] = int(row['price'])
        except ValueError:
            row['price'] = None
        data.append(row)

data_json = json.dumps(data, ensure_ascii=False, indent=2)
print(data_json)
