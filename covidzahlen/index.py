import http.client
import json

conn = http.client.HTTPSConnection("covid-19-statistics.p.rapidapi.com")

headers = {
    'x-rapidapi-key': "6bf9bf4f6emshfd176586f689aa9p1055e6jsn0d347582fced",
    'x-rapidapi-host': "covid-19-statistics.p.rapidapi.com"
    }

conn.request("GET", "/reports?iso=DEU&date=2021-02-22", headers=headers)

res = conn.getresponse()
data = res.read()

testdata = json.loads(data)

for states in testdata["data"]:
    print(states["region"]["province"])
