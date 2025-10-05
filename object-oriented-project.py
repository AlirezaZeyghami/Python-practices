import random


class Human:
    def __init__(self, name):
        self.name = name


class Player(Human):
    def __init__(self, name):
        super().__init__(name)
        self.team = None

    def set_team(self, team):
        self.team = team


names = ["Hossein", "Maziar", "Akbar", "Nima", "Mahdi", "Farhad", "Mohammad", "Khashayar", "Milad", "Mostafa", "Amin",
         "Said", "Pouya", "Pourya", "Reza", "Ali", "Behzad", "Soheil", "Behrouz", "Shahrouz", "Saman", "Mohsen"]

auth_players = [Player(name) for name in names]


def team_setup(players):
    random.shuffle(players)
    a = players[:11]
    b = players[11:]

    for team_member in a:
        team_member.set_team("A")

    for team_member in b:
        team_member.set_team("B")

    return a, b


team_a, team_b = team_setup(auth_players)

for player in team_a + team_b:
    print(f"{player.team}: {player.name}")
