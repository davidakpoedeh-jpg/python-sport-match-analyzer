class MatchAnalyzer:
    def predict_match(self, previous_matches):
        if len(previous_matches) == 0:
            return "No prediction available."
        wins = 0
        for match in previous_matches:
            home = match["intHomeScore"]
            away = match["intAwayScore"]
            if home is not None and away is not None:
                if int(home) > int(away):
                    wins += 1
        if wins >= 3:
            return "Prediction: Team is likely to win."
        else:
            return "Prediction: Match may be difficult."
    def match_summary(self, match):
        return (
            f"{match['strHomeTeam']} played against "
            f"{match['strAwayTeam']}.\n"
            f"Score: {match['intHomeScore']} - "
            f"{match['intAwayScore']}"
        )