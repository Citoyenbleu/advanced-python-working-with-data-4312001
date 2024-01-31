# Example file for Advanced Python: Working With Data by Joe Marini
# Programming challenge: summarize the earthquake data

import json


# for this challenge, we're going to summarize the earthquake data as follows:
# 1: How many quakes are there in total?
# 2: How many quakes were felt by at least 100 people?
# 3: Print the name of the place whose quake was felt by the most people, with the # of reports
# 4: Print the top 10 most significant events, with the significance value of each

# open the data file and load the JSON
with open("30DayQuakes.json", "r") as datafile:
    data = json.load(datafile)


def felt_filter(q):
    if q["properties"]["felt"] is not None and q["properties"]["felt"] >= 100:
        return True
    return False


def get_felt(q):
    felt = q["properties"]["felt"]
    
    if felt is None:
        felt = 0
    return felt


def get_sig(q):
    sig = q["properties"]["sig"]

    if sig is None:
        sig = 0
    return float(sig)

quakes = len(data["features"])
felt_events = list(filter(felt_filter, data["features"]))
max_felt_quake = max(data["features"], key=get_felt)
most_reports_place = max_felt_quake["properties"]["place"]
most_reports = max_felt_quake["properties"]["felt"]


print(f"Number of quakes: {quakes}")
print(f"Number of events felt by 100 or more people: {len(felt_events)}")
print(f"Most felt reports: {most_reports_place}, {most_reports}")

data["features"].sort(key=get_sig, reverse=True)
for i in range(0, 10):
    title = data["features"][i]["properties"]["title"]
    sig = data["features"][i]["properties"]["sig"]

    print(f"Event: {title}, Sig: {sig}")

