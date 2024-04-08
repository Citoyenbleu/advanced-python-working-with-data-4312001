# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: use advanced data collections on the earthquake data

import json
import csv
import pprint
import datetime


# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)

# Create a CSV file with the following information:
# 40 most significant seismic events, ordered by most recent
# Header row: Magnitude, Place, Felt Reports, Date, and Google Map link
# Date should be in the format of YYYY-MM-DD

def get_sig(data):
    sig = data["properties"]["sig"]

    if sig is None:
        sig = 0
    
    return sig

sig_data = sorted(data["features"], key=get_sig, reverse=True)
sig_data = sig_data[:40]
print(sig_data)
sig_data.sort(key=lambda e: e["properties"]["time"], reverse=True)
print(sig_data)

header = ["mag", "place", "felt", "date", "link"]
rows = []
for event in sig_data:
    lat = event["geometry"]["coordinates"][1]
    long = event["geometry"]["coordinates"][0]
    link = f"https://maps.google.com/maps/search/?api=1&query={lat}%2C{long}"

    rows.append(
        [
            event["properties"]["mag"],
            event["properties"]["place"],
            event["properties"]["felt"] if event["properties"]["felt"] else 0,
            str(datetime.date.fromtimestamp(event["properties"]["time"]/1000)),
            link
        ]
    )
print(rows)

with open ("challenge_chp3.csv", "w") as csvfile:
    writer = csv.writer(csvfile, delimiter=',')
    writer.writerow(header)
    writer.writerows(rows)

