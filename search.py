import http.client
import csv

conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': "apikey 0F5C2fpkXXs4ltJSljxH45:3UcatViBkDsMbXz4zXzcEV"
    }

conn.request("GET", "/gasPrice/stateUsaPrice?state=CA", headers=headers)

res = conn.getresponse()
data = res.read()

# print(data.decode("utf-8"))

# file = open("Salary_Data.csv")
# csvreader = csv.reader(file)
# header = next(csvreader)
# print(header)
# rows = []
# for row in data:
#     rows.append(data)
# print(rows)
# file.close()

f = open("response.text", "w")
o =  open("response.csv", "a")
rows = []
rows.append(data)
# print(rows)
# f.write(rows)


# list1 = [1, 2, 3]
str1 = ''.join(str(e) for e in rows)
# print(str1)
# o.write(str1)
# print(str1.find("San Diego"))

# print(str1[2549:2639])
# print(str1[2560:2565])

# if "Los Angeles" in str1:
    #print("True")
# f.write("Average gas prices in San Diego are: "+ str1[2549:2639])
result = str1.find("Los Angeles")
# print("Found at index: ", result)
losAngeles = str1[result-50: result-45]
# print(losAngeles)
value = input()
# print(value)
if value in str1:
    # print("True")
    result2 = str1.find(value)
    # print(result2)
    print("The current gas prices are: $" + str1[result2-50:result2-45])

