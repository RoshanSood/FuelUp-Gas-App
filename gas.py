import csv
from urllib import request
file = open("response.csv")
csvreader = csv.reader(file)
header = next(csvreader)
print(header)
rows = []
for row in csvreader:
    rows.append(row)
# print(rows)
file.close()

# url = 'https://gasprices.aaa.com/?state=CA'

# # Connect to the URL
# response = request.get(url)
# print(response)