# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
from collections import Counter


# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

events = []
for event in data["features"]:
    events.append(event["properties"]["type"])

count = Counter(events)

for key, value in count.items():
    print(f"{key:15} : {value}")
