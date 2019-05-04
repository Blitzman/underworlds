import json

warbands_ = []

with open('warbands.json') as _f:
    warbands_json_ = json.load(_f)

    for season in warbands_json_:
        warbands_.extend(warbands_json_[season])

#print(warbands_)

matches_ = []

with open('matches.json') as _f:
    matches_json_ = json.load(_f)

    for match in matches_json_:
        matches_.append(match)

def create_player():

    player_ = {}
    player_["games"] = 0
    player_["win"] = 0
    player_["draw"] = 0
    player_["lost"] = 0
    player_["glory_scored"] = 0
    player_["glory_conceded"] = 0

    return player_


players_ = {}

for i in range(len(matches_)):

    #print(matches_[i])

    player_a_ = matches_[i]["player_a"]
    player_b_ = matches_[i]["player_b"]

    if (not player_a_ in players_):
        players_[player_a_] = create_player()

    if (not player_b_ in players_):
        players_[player_b_] = create_player()

    if matches_[i]["winner"] == player_a_:
        players_[player_a_]["win"] += 1
        players_[player_b_]["lost"] += 1
    elif matches_[i]["winner"] == player_b_:
        players_[player_b_]["win"] += 1
        players_[player_a_]["lost"] += 1
    elif matches_[i]["winner"] == "Draw":
        players_[player_b_]["draw"] += 1
        players_[player_a_]["draw"] += 1
    else:
        print("INVALID MATCH")
        continue

    players_[player_a_]["games"] += 1
    players_[player_a_]["glory_scored"] += matches_[i]["glory_a"]
    players_[player_a_]["glory_conceded"] += matches_[i]["glory_b"]

    players_[player_b_]["games"] += 1
    players_[player_b_]["glory_scored"] += matches_[i]["glory_b"]
    players_[player_b_]["glory_conceded"] += matches_[i]["glory_a"]
    
#print(players_)

def print_player_stats(players):

    print("Player \t Games \t Win \t\t Draw \t\t Loss \t\t Glory(w:c:b)")

    for p in players:

        print("{} \t {} \t {}({:.2f}%) \t {}({:.2f}%) \t {}({:.2f}%) \t {}:{}:{}".format(
            p,
            players[p]["games"],
            players[p]["win"],
            players[p]["win"] * 100.0 / players[p]["games"],
            players[p]["draw"],
            players[p]["draw"] * 100.0 / players[p]["games"],
            players[p]["lost"],
            players[p]["lost"] * 100.0 / players[p]["games"],
            players[p]["glory_scored"],
            players[p]["glory_conceded"],
            players[p]["glory_scored"] - players[p]["glory_conceded"],
        ))

print_player_stats(players_)