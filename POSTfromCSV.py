import csv
from urllib import request, parse

URL = "https://reqres.in/api/users"
filename = "data.csv"
data_list = []
count = 0
with open(filename, 'r') as f:
    for line in csv.DictReader(f):
        print(line)
        data_list.append(line)
        data = parse.urlencode(data_list[count]).encode()

        req = request.Request(URL, data, headers={'User-Agent': 'Mozilla/5.0'})
        print(req)
        response = request.urlopen(req)
        count = count + 1

        print(response.getcode())
