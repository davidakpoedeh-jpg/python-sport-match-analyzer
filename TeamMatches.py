class Team:
    def __init__(self, name, country, coach):
        self.name = name
        self.country = country
        self.coach = coach

    def __str__(self):
        return f"Team: {self.name}, Country: {self.country}, Coach: {self.coach}"


class Match:
    def __init__(self, home_team, away_team, date, score):
        self.home_team = home_team
        self.away_team = away_team
        self.date = date
        self.score = score

    def __str__(self):
        return f"{self.home_team} vs {self.away_team} on {self.date}. Score: {self.score}"


team1 = Team("Arsenal", "England", "Mikel Arteta")
team2 = Team("Chelsea", "England", "Enzo Maresca")

print(team1)
print(team2)

match1 = Match("Arsenal", "Chelsea", "20/06/2026", "2-1")

print(match1)