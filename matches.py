import json

warbands_ = []

with open('warbands.json') as _f:
    warbands_json_ = json.load(_f)

    for season in warbands_json_:
        warbands_.extend(warbands_json_[season])

print(warbands_)

matches_ = []

with open('matches.json') as _f:
    matches_json_ = json.load(_f)

    for match in matches_json_:
        matches_.append(match)

print(matches_)