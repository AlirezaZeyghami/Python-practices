teams = {
    "Iran": {"wins": 0, "loses": 0, "draws": 0, "goal_diff": 0, "points": 0},
    "Portugal": {"wins": 0, "loses": 0, "draws": 0, "goal_diff": 0, "points": 0},
    "Spain": {"wins": 0, "loses": 0, "draws": 0, "goal_diff": 0, "points": 0},
    "Morocco": {"wins": 0, "loses": 0, "draws": 0, "goal_diff": 0, "points": 0}
}

games = [
    ("Iran", "Spain"),
    ("Iran", "Portugal"),
    ("Iran", "Morocco"),
    ("Spain", "Portugal"),
    ("Spain", "Morocco"),
    ("Portugal", "Morocco")
]


def update_result(team1, team2, g1, g2):
    teams[team1]["goal_diff"] += g1 - g2
    teams[team2]["goal_diff"] += g2 - g1

    if g1 > g2:
        teams[team1]["wins"] += 1
        teams[team2]["loses"] += 1
        teams[team1]["points"] += 3
    elif g1 < g2:
        teams[team2]["wins"] += 1
        teams[team1]["loses"] += 1
        teams[team2]["points"] += 3
    else:
        teams[team1]["draws"] += 1
        teams[team2]["draws"] += 1
        teams[team1]["points"] += 1
        teams[team2]["points"] += 1


for t1, t2 in games:
    g1, g2 = map(int, input().split("-"))
    update_result(t1, t2, g1, g2)

sorted_teams = sorted(
    teams.items(),
    key=lambda x: (-x[1]["points"], -x[1]["wins"], x[0])
)

for name, stats in sorted_teams:
    print(f"{name} wins:{stats['wins']} , loses:{stats['loses']} , "
          f"draws:{stats['draws']} , goal difference:{stats['goal_diff']} , points:{stats['points']}")
