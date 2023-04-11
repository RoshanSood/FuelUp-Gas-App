import http.client

conn = http.client.HTTPSConnection("api.collectapi.com")

headers = {
    'content-type': "application/json",
    'authorization': "apikey 0F5C2fpkXXs4ltJSljxH45:3UcatViBkDsMbXz4zXzcEV"
    }

conn.request("GET", "/time/timezone?data.city=paris", headers=headers)

res = conn.getresponse()
data = res.read()

print(data.decode("utf-8"))
